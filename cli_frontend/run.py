#!/usr/bin/python3
import server.models as md
from server.models.city import City
from server.models.amenity import Amenity
from server.models.client import Client
from server.models.gym import Gym
from server.models.owner import Owner
from server.models.review import Review
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.requests import Request
from server.models import storage


app = FastAPI()
app.mount("/cli_frontend", StaticFiles(directory="cli_frontend"), name="static")

templates = Jinja2Templates(directory="cli_frontend/public")

@app.get("/home/")
async def home_redirect():
    return RedirectResponse(url="/")

@app.get("/")
async def home(request: Request):
    all_gymes = md.storage.all(Gym).values()
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "data": all_gymes
        }
    )

@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {
            "request": request,
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
@app.get("/user")
async def home(request: Request):
    all_gymes = md.storage.all(Gym).values()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "data": all_gymes
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
    # return gym.to_dict()
    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
            "gym": gym
        }
    )
