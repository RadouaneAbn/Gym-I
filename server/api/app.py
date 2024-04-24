#!/usr/bin/python3

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from server.api.views.clients import client_router
from server.api.views.owners import owner_router
from server.api.views.amenities import amenity_router
from server.api.views.cities import city_router
from server.api.views.gymes import gym_router

app = FastAPI()
app.include_router(client_router)
app.include_router(owner_router)
app.include_router(amenity_router)
app.include_router(city_router)
app.include_router(gym_router)

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc: HTTPException):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"error": "Not found"},
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )