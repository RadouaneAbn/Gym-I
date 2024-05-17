#!/usr/bin/python3
""" End points resposible for the authentication """
from fastapi import APIRouter, Depends
from server.models.client import Client
from server.auth.auth import check_token

auth_router = APIRouter()


@auth_router.get("/token_check/")
async def client_login(user: Client = Depends(check_token)):
    """ This function returns a Client if a JWT token is valid """
    return {"user": user.to_dict()}
