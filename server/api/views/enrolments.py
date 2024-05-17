""" Enrolment router """
from server.models.client import Client
from fastapi import APIRouter, Depends
from server.models.client import Client
from server.models.membership import EnrolClient
from server.api.schemas.all_schemas import EnrolData
from server.auth.auth import check_token
from datetime import datetime
from dateutil.relativedelta import relativedelta
from starlette.status import HTTP_200_OK


enrolment_router = APIRouter()


@enrolment_router.get("/client/gyms")
async def get_client_gyms(user: Client = Depends(check_token)):
    """ This end point returns all purchases made by client """
    return {
        "gyms": [purchase.to_dict() for purchase in user.enrolments]
        }, HTTP_200_OK


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
    return new_sub.to_dict(), HTTP_200_OK
