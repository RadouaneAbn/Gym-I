#!/usr/bin/python3
import server.models as md
from server.models.city import City
from server.models.amenity import Amenity
from server.models.client import Client
from server.models.gym import Gym
from server.models.owner import Owner
from server.models.review import Review
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware


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


@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
        }
    )


@app.get("/register")
async def login(request: Request):
    return templates.TemplateResponse(
        "register.html",
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
