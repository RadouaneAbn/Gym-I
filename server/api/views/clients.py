#!/usr/bin/python3
from fastapi import APIRouter, Depends, UploadFile, Form, File
from server.models.client import Client
from server.models import storage
from fastapi import FastAPI, HTTPException
from server.api.schemas.client_schema import (
    ClientModel, ClientModelPUT, ClientModelPWD, EmailCheck, ClientLogin)
from server.api.schemas.token_schema import *
from hashlib import md5
from server.models.hash import Hash
from starlette.status import HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED, HTTP_201_CREATED
from datetime import datetime, timedelta
from jose import JWTError, jwt
# from server.models.engine.secure import oauth_2_scheme
from typing_extensions import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
import requests
from server.models.engine.secure import verify_password
from server.models.extra import resize_128
from server.auth.auth import check_token
import requests


oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
IMG_BB_TOKEN = "dfcbe0e16596fd0c2dbb83c94c90718b"
IMG_BB_URL = "https://api.imgbb.com/1/upload"
IMG_SIZE = (128, 128)


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
    if verify_password(client.old_password, target_client.password):
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
    if not verify_password(password, user.password):
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED,
                            detail="Incorrect password")
    return user

def create_access_token(info: dict, expires_delta: timedelta = timedelta(minutes=15)):
    data = info.copy()
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


# @client_router.post("upload_profile_picture")
# async def upload_picture(img: UploadFile, token:str = Depends)

# @client_router.post("/uploadtest")
# async def testupload(file_upload: UploadFile):
#     file_upload = file_upload.file.read()
#     payload = {
#         "key": IMG_BB_TOKEN,
#         "image": file_upload
#     }
#     res = requests.post(IMG_BB_URL, files={"image": file_upload}, data=payload)
#     print(res.json()["data"]["display_url"])

@client_router.post("/clients/")
async def create_client(file_upload: UploadFile = None,
                        first_name: str = Form(...),
                        last_name: str = Form(...),
                        email: str = Form(...),
                        password: str = Form(...)):
    
    new_client = Client(**{
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password
    })
    if file_upload:
        img = file_upload.file.read()
        img_128 = resize_128(img)
        payload = {
            "key": IMG_BB_TOKEN
        }
        payload_resized_img = {
            "key": IMG_BB_TOKEN
        }
        res = requests.post(IMG_BB_URL, files={"image": img}, data=payload)
        res_resize = requests.post(IMG_BB_URL, files={"image": img_128}, data=payload_resized_img)

        print(res.json())

        # setattr(new_client, "profile_picture", res_resize.json()["data"]["display_url"])
        # setattr(new_client, "profile_picture_original", res.json()["data"]["display_url"])
        new_client.profile_picture = res_resize.json()["data"]["display_url"]
        new_client.profile_picture_original = res.json()["data"]["display_url"]

    # print(new_client)
    new_client.save()
    return {"detail": "User created successfuly"}, HTTP_201_CREATED

def upload_picture(img, img_128, payload):
    res = requests.post(IMG_BB_URL, files={"image": img}, data=payload)
    res_resize = requests.post(IMG_BB_URL, files={"image": img_128}, data=payload)

    return {
        "normal_p": res.json()["data"]["display_url"],
        "resized_p": res_resize.json()["data"]["display_url"],
        "delete": [res.json()["data"]["delete_url"], res_resize.json()["data"]["delete_url"]]
    }

@client_router.put("/profile_picture/")
def update_profile_picture(file_upload: UploadFile = None,
                           user: Client = Depends(check_token)):
    img = file_upload.file.read()
    img_128 = resize_128(img)
    payload = {
            "key": IMG_BB_TOKEN
    }

    upload_info = upload_picture(img, img_128, payload)

    user.profile_picture = upload_info["resized_p"]
    user.profile_picture_original = upload_info["normal_p"]
    user.delete_urls = upload_info["delete"]

    print(user)

    user.save()

    return {"detail": "profile picture updated successfuly"}, 200

def delete_picture(user):
    print(user)
    response = requests.delete(user.delete_urls[0], params={"url": user.profile_picture_original})
    response_2 = requests.delete(user.delete_urls[1], params={"url": user.profile_picture})
    return response.status_code, response_2.status_code

@client_router.delete("/profile_picture/{user_id}")
def delete_client_profile_picture(user_id: str):
    user = storage.get(Client, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")
    user.profile_picture = None
    user.profile_picture_original = None
    user.save()
    return {"details": "Picture deleted successfuly"}
