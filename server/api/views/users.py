from fastapi import APIRouter, Depends
from server.models.client import Client
from server.models.owner import Owner
from server.auth.auth import check_token
from typing import Union

user_router = APIRouter()

@user_router.get('/users/')
async def get_user_info(user: Union[Client, Owner] = Depends(check_token)):
    return {"user_info": user.to_dict(pop=["profile_picture_original"])}
