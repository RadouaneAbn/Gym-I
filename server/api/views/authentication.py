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

SECRET_KEY = "4f0e2935cdf27d24222357163158cb6d481bc67c5e15c2eaa1c5982ecf3e80b1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


auth_router = APIRouter()


def check_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="Authorization header missing or invalid")
    try:
        token = authorization[7:]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # print("payload:", payload)
        email = payload.get("sub")
        exp = payload.get("exp")
        print(datetime.utcfromtimestamp(exp), datetime.utcnow())
        if datetime.utcfromtimestamp(exp) <= datetime.utcnow():
        # if exp <= datetime.utcnow.timestamp():
            raise HTTPException(status_code=401, detail="Token expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return storage.get_user(Client, email)


@auth_router.get("/token_check/")
async def client_login(user: Client = Depends(check_token)):
    return {"user": user}