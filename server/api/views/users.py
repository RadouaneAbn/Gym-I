""" This models holds some function used by Owner and Client
"""

from fastapi import APIRouter, Depends
from server.models.client import Client
from server.models.owner import Owner
from server.auth.auth import check_token
from typing import Union

user_router = APIRouter()


@user_router.get('/users/')
async def get_user_info(user: Union[Client, Owner] = Depends(check_token)):
    """ This endpoint returns a link to the profile picture """
    return {"profile_pic": user.profile_picture}
