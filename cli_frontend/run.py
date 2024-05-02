#!/usr/bin/python3
import server.models as md
from server.models.city import City
from server.models.amenity import Amenity
from server.models.client import Client
from server.models.gym import Gym
from server.models.owner import Owner
from server.models.review import Review
from fastapi import FastAPI, HTTPException, status, Depends
from server.models.engine.secure import Secure
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from server.models import storage
from server.api.schemas.client_schema import (
    ClientModel, ClientModelPUT, ClientModelPWD, EmailCheck, ClientLogin)
from starlette.status import HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED
from server.models.hash import Hash
from datetime import datetime, timedelta
from server.api.schemas.token_schema import *
from typing_extensions import Annotated

from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from functools import wraps
from fastapi import Request

oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")


SECRET_KEY = "4f0e2935cdf27d24222357163158cb6d481bc67c5e15c2eaa1c5982ecf3e80b1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except HTTPException as exc:
            if exc.status_code == 401:  # Catch 401 Unauthorized
                return RedirectResponse(url="/signin")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,  # Allow cookies and authentication headers
    allow_methods=["*"],  # Allowed HTTP methods
    allow_headers=["*"],  # Allow all headers
)
app.add_middleware(AuthMiddleware)

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

@app.get("/register")
async def about(request: Request):
    return templates.TemplateResponse(
        "register.html",
        {
            "request": request,
        }
    )

# @app.get("/{user_id}")
# async def user(user_id: str, request: Request):
#     user = storage.get(Client, user_id)
#     all_gymes = md.storage.all_list(Gym)
#     return templates.TemplateResponse(
#         "userpage.html",
#         {
#             "request": request,
#             "user": user,
#             "data": all_gymes
#         }
#     )

@app.get("/signin")
async def about(request: Request):
    return templates.TemplateResponse(
        "signin.html",
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

def authenticate_user(email, password):
    user = storage.get_user(Client, email)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Email does not exist")
    if not Hash.validate_pwd(password, user.password):
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED,
                            detail="Incorrect password")
    return user

def create_access_token(info: dict, expires_delta: timedelta = timedelta(minutes=15)):
    data = info.copy()
    # print("data = ", data)
    expire = datetime.utcnow() + timedelta(minutes=1)
    data.update({"exp": expire})
    # print(expire)

    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt 

async def get_current_user(token: Annotated[str, Depends(oauth_2_scheme)]):
    print("token:", token)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("payload:", payload)
        email = payload.get("sub")
        exp = payload.get("exp")
        # print(datetime.utcfromtimestamp(exp), datetime.utcnow())
        if datetime.utcfromtimestamp(exp) <= datetime.utcnow():
        # if exp <= datetime.utcnow.timestamp():
            raise HTTPException(status_code=401, detail="Token expired")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = storage.get_user(Client, email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def token_required(func):
    @wraps(func)
    def decorated(request: Request, *args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
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
    return decorated


@app.get("/me", status_code=status.HTTP_200_OK)
@token_required
async def get_current_user_info(request: Request):
    return templates.TemplateResponse(
        "userpage.html",
        {
            "request": request
        }
    )


# @app.get("/me", status_code=status.HTTP_200_OK)
# async def get_current_user_info(user: Annotated[dict, Depends(get_current_user)],
#                                 request: Request):
#     if not user:
#         return RedirectResponse(url="/signin")
#     return templates.TemplateResponse(
#         "userpage.html",
#         {
#             "request": request,
#             "user": user
#         }
#     )