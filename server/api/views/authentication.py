#!/usr/bin/python3

from fastapi import APIRouter, Depends, Header, HTTPException
from server.models.city import City
from server.models import storage
from fastapi import HTTPException
from server.api.schemas.city_schema import CityModel
from fastapi.responses import HTMLResponse, RedirectResponse
from jose import JWTError, jwt
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from functools import wraps
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from server.models.client import Client
from server.auth.auth import check_token

auth_router = APIRouter()


@auth_router.get("/token_check/")
async def client_login(user: Client = Depends(check_token)):
    return {"user": user.to_dict()}
