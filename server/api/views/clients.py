#!/usr/bin/python3
from fastapi import APIRouter, Depends
from server.models.client import Client
from server.models import storage
from fastapi import FastAPI, HTTPException
from server.api.schemas.client_schema import (
    ClientModel, ClientModelPUT, ClientModelPWD, EmailCheck, ClientLogin)
from server.api.schemas.token_schema import *
from hashlib import md5
from server.models.hash import Hash
from starlette.status import HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED
from datetime import datetime, timedelta
from jose import JWTError, jwt
# from server.models.engine.secure import oauth_2_scheme
from typing_extensions import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware


oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


SECRET_KEY = "4f0e2935cdf27d24222357163158cb6d481bc67c5e15c2eaa1c5982ecf3e80b1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

client_router = APIRouter()


@client_router.get("/clients/")
async def get_users():
    return [client.to_dict() for client in storage.all(Client).values()]

@client_router.get("/clients/{client_id}")
async def get_user(client_id: str):
    client = storage.get(Client, client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return client.to_dict(True)

@client_router.post("/clients/")
async def create_client(client: ClientModel):
    new_client = Client(**client.__dict__)
    new_client.save()

@client_router.put("/clients/{client_id}")
async def update_user(client_id: str, client: ClientModelPUT):
    ignore = ["email", "id", "created_id", "updated_at"]
    inst = storage.get(Client, client_id)
    if inst is None:
        raise HTTPException(status_code=404, detail="Not Found")

    for key, value in client.__dict__.items():
        if key in ignore or not value:
            continue
        setattr(inst, key, value)
    inst.save()

@client_router.put("/clients/password/{client_id}")
async def update_user_password(client_id: str, client: ClientModelPWD):
    target_client = storage.get(Client, client_id)
    hashed_new_password = md5(client.old_password.encode()).hexdigest()
    if target_client.password != hashed_new_password:
        raise HTTPException(status_code=401, detail="Wrong password")
    
    target_client.password = client.new_password
    target_client.save()

@client_router.delete("/clients/{client_id}/")
async def delete_client(client_id: str):
    client = storage.get(Client, client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Not Found")
    storage.delete(client)
    storage.save()

@client_router.post("/emailcheck/")
async def email_check(data: EmailCheck):
    print(data.email)
    return storage.email_exists(Client, data.email)


@client_router.post("/clients/login", response_model=Token)
# async def client_login(info: ClientLogin):
async def client_login(info: ClientLogin):
    user = authenticate_user(info.email, info.password)
    # print("user = ", user)
    token = create_access_token({
        "sub": user.email
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
    expire = datetime.utcnow() + timedelta(minutes=60)
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
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Outdated token")
        if email is None:
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Invalid token")
        user = storage.get_user(Client, email)
        if not user:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Invalid token")

