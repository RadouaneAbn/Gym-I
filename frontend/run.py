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


app = FastAPI()
app.mount("/frontend", StaticFiles(directory="frontend"), name="static")




templates = Jinja2Templates(directory="frontend/templates")

@app.get("/home/")
async def home_redirect():
    return RedirectResponse(url="/")

@app.get("/")
async def home(request: Request):
    all_gymes = md.storage.all(Gym).values()
    return templates.TemplateResponse(
        "index2.html",
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
