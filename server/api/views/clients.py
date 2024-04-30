#!/usr/bin/python3
from fastapi import APIRouter
from server.models.client import Client
from server.models import storage
from fastapi import FastAPI, HTTPException
from server.api.schemas.client_schema import (
    ClientModel, ClientModelPUT, ClientModelPWD, EmailCheck, ClientLogin)
from hashlib import md5
from server.models.hash import Hash


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

@client_router.post("/clients/login")
async def client_login(info: ClientLogin):
    user = storage.get_user(Client, info.email)
    print(user)
    if not user:
        return False
    if not Hash.validate_pwd(info.password, user.password):
        return False

    return user.to_dict()