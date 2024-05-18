#!/usr/bin/python3
""" App: the back-end points starter """
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# all routers
from server.api.views.clients import client_router
from server.api.views.owners import owner_router
from server.api.views.amenities import amenity_router
from server.api.views.cities import city_router
from server.api.views.gymes import gym_router
from server.api.views.gym_filter import gym_filter
from server.api.views.authentication import auth_router
from server.api.views.users import user_router
from server.api.views.enrolments import enrolment_router

PREFIX = "/api/v1"


app = FastAPI()
app.include_router(client_router, prefix=PREFIX)
app.include_router(owner_router, prefix=PREFIX)
app.include_router(amenity_router, prefix=PREFIX)
app.include_router(city_router, prefix=PREFIX)
app.include_router(gym_router, prefix=PREFIX)
app.include_router(gym_filter, prefix=PREFIX)
app.include_router(auth_router, prefix=PREFIX)
app.include_router(user_router, prefix=PREFIX)
app.include_router(enrolment_router, prefix=PREFIX)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,  # Allow cookies and authentication headers
    allow_methods=["*"],  # Allowed HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc: HTTPException):
    """ This function handles the error raised in the api endpoints """
    if exc.status_code == 404:  # not found
        return JSONResponse(
            status_code=404,
            content={"error": "Not found"},
        )
    elif exc.status_code == status.HTTP_401_UNAUTHORIZED:  # unauthorized
        return JSONResponse(status_code=exc.status_code,
                            content={"status": False})

    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )
