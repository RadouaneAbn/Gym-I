#!/usr/bin/python3

from server.models.client import Client
from server.models.gym import Gym

from fastapi import APIRouter, Depends, UploadFile, Form, File
from server.models.client import Client
from server.models import storage
from fastapi import FastAPI, HTTPException
from server.api.schemas.token_schema import *
from hashlib import md5
from server.models.hash import Hash
from starlette.status import HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED, HTTP_201_CREATED

client_router = APIRouter()

# @client_router.get()