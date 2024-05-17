#!/usr/bin/python3
from server.models.client import Client
from server.models.gym import Gym
from fastapi import APIRouter, Depends, UploadFile, Form, File
from server.models.client import Client
from server.models import storage
from server.models.membership import EnrolClient
from fastapi import FastAPI, HTTPException
from server.api.schemas.enrolment_schema import GetEnroleAll, EnrolData
from hashlib import md5
from server.models.hash import Hash
from starlette.status import HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED, HTTP_201_CREATED
from server.auth.auth import check_token
from datetime import datetime
from dateutil.relativedelta import relativedelta

enrolment_router = APIRouter()

@enrolment_router.get("/client/gyms")
async def get_client_gyms(user: Client = Depends(check_token)):
    return {"gyms": [purchase.to_dict() for purchase in user.enrolments]}

@enrolment_router.post("/client/gyms/enrol")
async def enrole_client_gym(data: EnrolData, user: Client = Depends(check_token)):
    start_date = datetime.strptime(data.date, '%Y-%m-%d')
    new_sub = EnrolClient(
        payment_id=data.payment_id,
        client_id=user.id,
        gym_id=data.gym_id,
        from_date=start_date,
        to_date=start_date + relativedelta(months=int(data.months))
    )

    new_sub.save()
    return new_sub.to_dict()

# API enpoint to retrieve all history of payement for client
@enrolment_router.get("/clients/history/")
async def get_client_history(user: Client = Depends(check_token)):
    history = [enroll.to_dict() for enroll in user.enrolments]
    for payment in history:
        payment['gym_name'] = storage.get(Gym, payment["gym_id"]).name
    return history

