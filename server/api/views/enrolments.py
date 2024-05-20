""" Enrolment router """
from server.models.client import Client
from fastapi import APIRouter, Depends
from server.models.client import Client
from server.models.membership import EnrolClient
from server.api.schemas.all_schemas import EnrolData
from server.auth.auth import check_token
from datetime import datetime
from dateutil.relativedelta import relativedelta
from server.models import storage
from server.models.gym import Gym


enrolment_router = APIRouter()


@enrolment_router.get("/client/gyms")
async def get_client_gyms(user: Client = Depends(check_token)):
    """ This end point returns all purchases made by client """
    return {
        "gyms": [purchase.to_dict() for purchase in user.enrolments]
        }


@enrolment_router.post("/client/gyms/enrol")
async def enrole_client_gym(data: EnrolData,
                            user: Client = Depends(check_token)):
    """ This function create a puchase history if a payment is successful """
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
    """ Return the purchase history of a Client """
    history = [enroll.to_dict() for enroll in user.enrolments]
    for payment in history:
        payment['gym_name'] = storage.get(Gym, payment["gym_id"]).name
    return history

