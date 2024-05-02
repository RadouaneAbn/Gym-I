#!/usr/bin/python3

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from server.api.views.clients import client_router
from server.api.views.owners import owner_router
from server.api.views.amenities import amenity_router
from server.api.views.cities import city_router
from server.api.views.gymes import gym_router
from server.api.views.gym_amenities import gym_amenity_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse


app = FastAPI()
app.include_router(client_router)
app.include_router(owner_router)
app.include_router(amenity_router)
app.include_router(city_router)
app.include_router(gym_router)
app.include_router(gym_amenity_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,  # Allow cookies and authentication headers
    allow_methods=["*"],  # Allowed HTTP methods
    allow_headers=["*"],  # Allow all headers
)



@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc: HTTPException):
    print(exc.status_code)
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"error": "Not found"},
        )
    elif exc.status_code == status.HTTP_401_UNAUTHORIZED:
        return RedirectResponse(url="/signin")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )
