#!/usr/bin/python3
import server.models as md
from server.models.city import City
from server.models.amenity import Amenity
from server.models.client import Client
from server.models.gym import Gym
from server.models.owner import Owner
from server.models.review import Review
from fastapi import FastAPI, HTTPException, Query, Form, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.requests import Request
from server.models import storage
from typing import Optional, List
from server.api.views.clients import authenticate_user, create_access_token

from server.api.schemas.client_schema import ClientLogin

from jose import JWTError, jwt
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from functools import wraps
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta

oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


SECRET_KEY = "4f0e2935cdf27d24222357163158cb6d481bc67c5e15c2eaa1c5982ecf3e80b1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


app = FastAPI()
app.mount("/cli_frontend", StaticFiles(directory="cli_frontend"), name="static")

templates = Jinja2Templates(directory="cli_frontend/public")

@app.get("/home/")
async def home_redirect():
    return RedirectResponse(url="/")

@app.get("/")
async def home(request: Request):
    all_gymes = md.storage.all_list(Gym)[:5]
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "data": all_gymes[:10]
        }
    )

@app.get("/offers")
async def home(request: Request):
    all_gymes = md.storage.all(Gym).values()
    for gym in all_gymes:
        setattr(gym, "city", md.storage.get(City, gym.city_id).name)

    return templates.TemplateResponse(
        "offers.html",
        {
            "request": request,
            "data": all_gymes
        }
    )
@app.get("/signin")
async def about(request: Request):
    return templates.TemplateResponse(
        "signin.html",
        {
            "request": request,
        }
    )

@app.get("/register")
async def about(request: Request):
    return templates.TemplateResponse(
        "register.html",
        {
            "request": request,
        }
    )

@app.post("/token")
# async def client_login(info: ClientLogin):
async def client_login(info: ClientLogin):
    user = authenticate_user(info.email, info.password)
    # print("user = ", user)
    token = create_access_token({
        "sub": user.email,
        "id": user.id
    })
    return {"access_token": token, "token_type": "bearer"}

@app.get("/user/gymes_test")
async def home_test(request: Request, page: int = Query(1, description="Page number", gt=0)):
    all_gymes = md.storage.get_page(Gym, page)
    for gym in all_gymes:
        setattr(gym, "city_name", storage.get(City, gym.city_id).name)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "cities": storage.all_list(City),
            "amenities": storage.all_list(Amenity),
            "data": all_gymes,
            "count": storage.pages_count(Gym)
        }
    )

@app.get("/profile")
async def about(request: Request):
    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
        }
    )

@app.get("/user/gymes/{gym_id}")
async def get_gym_info(gym_id: str, request: Request):
    gym = storage.get(Gym, gym_id)
    if gym is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return templates.TemplateResponse(
        "gym.html",
        {
            "request": request,
            "amenities": [am.name for am in gym.amenities],
            "gym": gym.to_dict(pop=["amenities"]),
            "city_name": storage.get(City, gym.city_id).name
        }
    )

def check(token):
    if not token:
        print("no token here")
        return RedirectResponse(url="/signin")
    try:
        if token.startswith("Bearer "):
            token = token[7:]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # print("payload:", payload)
        email = payload.get("sub")
        exp = payload.get("exp")
        # print(datetime.utcfromtimestamp(exp), datetime.utcnow())
        if datetime.utcfromtimestamp(exp) <= datetime.utcnow():
        # if exp <= datetime.utcnow.timestamp():
            raise HTTPException(status_code=401, detail="Token expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return storage.get_user(Client, email)

@app.get("/user/gymes")
async def home(request: Request):
    all_gymes = md.storage.get_page(Gym, 1)
    for gym in all_gymes:
        setattr(gym, "city_name", storage.get(City, gym.city_id).name)
    return templates.TemplateResponse(
        "userhome.html",
        {
            "request": request,
            "cities": storage.all_list(City),
            "amenities": storage.all_list(Amenity),
            "count": storage.pages_count(Gym)
        }
    )

@app.get("/tp")
async def tp(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "cities": storage.all_list(City),
            "amenities": storage.all_list(Amenity),
            "count": storage.pages_count(Gym)
        }
    )
