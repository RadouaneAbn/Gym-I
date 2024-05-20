#!/usr/bin/python3
from fastapi import APIRouter, Depends, UploadFile, Form
from server.models.client import Client
from server.models import storage
from fastapi import HTTPException
from server.api.schemas.all_schemas import (
    ClientModelPUT, ClientModelPWD, EmailCheck, ClientLogin)
from server.api.schemas.all_schemas import *
from server.models.engine.secure import verify_password
from server.models.extra import resize_128, upload_picture
from server.auth.auth import *
from os import getenv

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 60

client_router = APIRouter()


@client_router.get("/clients/")
async def get_users():
    """ Return all clients """
    return [client.to_dict() for client in storage.all(
        Client).values()]


@client_router.get("/clients/{client_id}")
async def get_user(client_id: str):
    """ Return a client using its id """
    client = storage.get(Client, client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return client.to_dict(True)


@client_router.put("/clients/{client_id}")
async def update_user(client_id: str, client: ClientModelPUT):
    """ Update a client """
    ignore = ["email", "id", "created_id", "updated_at"]
    inst = storage.get(Client, client_id)
    if inst is None:
        raise HTTPException(status_code=404, detail="Not Found")

    for key, value in client.__dict__.items():
        if key in ignore or not value:
            continue
        setattr(inst, key, value)
    inst.save()
    return {"detail": "Client created successfully"}


@client_router.put("/clients/password/{client_id}")
async def update_user_password(client_id: str, client: ClientModelPWD):
    """ Change client password """
    target_client = storage.get(Client, client_id)
    if verify_password(client.old_password, target_client.password):
        raise HTTPException(status_code=401, detail="Wrong password")

    target_client.password = client.new_password
    target_client.save()
    return {"detail": "Password changed successfully"}


@client_router.delete("/clients/")
async def delete_client(user: Client = Depends(check_token)):
    """ Delete a client """
    storage.delete(user)
    storage.save()
    return {"detail": "Client deleted successfully"}


@client_router.post("/emailcheck/")
async def email_check(data: EmailCheck):
    """ return true if the given email is not already in the database """
    return storage.email_exists(Client, data.email)


@client_router.post("/clients/login", response_model=Token)
async def client_login(info: ClientLogin):
    """ Login process (authenticate the user then create a JWT token) """
    user = authenticate_user(info.email, info.password)
    # print("user = ", user)
    token = create_access_token({
        "sub": user.email
    })
    return {"access_token": token, "token_type": "bearer"}


@client_router.post("/clients/")
async def create_client(file_upload: UploadFile = None,
                        first_name: str = Form(...),
                        last_name: str = Form(...),
                        email: str = Form(...),
                        password: str = Form(...)):
    """ Register a client """
    new_client = Client(**{
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password
    })

    if file_upload:
        # if an image is given it will be uploadedto imgbb
        img = file_upload.file.read()
        img_128 = resize_128(img)

        new_client.profile_picture = upload_picture(img_128)
        new_client.profile_picture_original = upload_picture(img)

    new_client.save()
    return {"detail": "User created successfuly"}


@client_router.put("/profile_picture/")
def update_profile_picture(file_upload: UploadFile = None,
                           user: Client = Depends(check_token)):
    """ Update the profile picture of a client """
    # print(file_upload)
    img = file_upload.file.read()
    img_128 = resize_128(img)

    user.profile_picture = upload_picture(img_128)
    user.profile_picture_original = upload_picture(img)
    user.save()

    return {"detail": "profile picture updated successfuly"}


@client_router.delete("/profile_picture/{user_id}")
def delete_client_profile_picture(user_id: str):
    """ Delete the profile picture of a client """
    user = storage.get(Client, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")
    user.profile_picture = None
    user.profile_picture_original = None
    user.save()
    return {"details": "Picture deleted successfuly"}
