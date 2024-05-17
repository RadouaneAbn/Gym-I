#!/usr/bin/python3
import paypalrestsdk
import server.models as md
from server.models.city import City
from server.models.amenity import Amenity
from server.models.client import Client
from server.models.gym import Gym
from server.models.review import Review
from fastapi import FastAPI, HTTPException, Query, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.requests import Request
from server.models import storage
from server.api.views.clients import authenticate_user, create_access_token
from server.api.schemas.client_schema import ClientLogin
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime
from dateutil.relativedelta import relativedelta
from server.models.membership import EnrolClient
from os import getenv

paypalrestsdk.configure({
    "mode": "sandbox",
    "client_id": getenv("PAYPAL_CLIENT_ID"),
    "client_secret": getenv("PAYPAL_CLIENT_SECRET")
})

oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


app = FastAPI()
app.mount("/cli_frontend", StaticFiles(directory="cli_frontend"), name="static")

templates = Jinja2Templates(directory="cli_frontend/public")

@app.get("/home/")
async def home_redirect():
    return RedirectResponse(url="/")

@app.get("/")
async def home(request: Request):
    all_gymes = md.storage.all_list(Gym)[:5]
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "data": all_gymes[:10]
        }
    )

@app.get("/offers")
async def home(request: Request):
    all_gymes = md.storage.all(Gym).values()
    for gym in all_gymes:
        setattr(gym, "city", md.storage.get(City, gym.city_id).name)

    return templates.TemplateResponse(
        "offers.html",
        {
            "request": request,
            "data": all_gymes
        }
    )
@app.get("/signin")
async def about(request: Request):
    return templates.TemplateResponse(
        "signin.html",
        {
            "request": request,
        }
    )

@app.get("/register")
async def about(request: Request):
    return templates.TemplateResponse(
        "register.html",
        {
            "request": request,
        }
    )

@app.post("/token")
# async def client_login(info: ClientLogin):
async def client_login(info: ClientLogin):
    user = authenticate_user(info.email, info.password)
    # print("user = ", user)
    token = create_access_token({
        "sub": user.email,
        "id": user.id
    })
    return {"access_token": token, "token_type": "bearer"}

@app.get("/profile/")
async def about(request: Request):
    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
        }
    )

@app.get("/user/gymes/{gym_id}")
async def get_gym_info(gym_id: str, request: Request):
    gym = storage.get(Gym, gym_id)
    reviews = md.storage.all(Review).values()
    rv = []
    if gym is None:
        raise HTTPException(status_code=404, detail="Not Found")
    
    setattr(gym, "city", storage.get(City, gym.city_id).name)
    
    count = 0
    for review in reviews:
        if review.gym_id == gym_id and count < 3:
            count += 1
            review_data = {
                "user_name": md.storage.get(Client, review.client_id).first_name,
                "review_text": review.text,
                "review_date": review.updated_at.strftime("%Y-%m-%d")
            }
            rv.append(review_data)
    
    return templates.TemplateResponse(
        "gym.html",
        {
            "request": request,
            "gym": gym.to_dict(),
            "reviews": rv,
            "amenities": [am.name for am in gym.amenities],
            "date": datetime.now().strftime('%Y-%m-%d')
        }
    )

def check(token):
    if not token:
        print("no token here")
        return RedirectResponse(url="/signin")
    try:
        if token.startswith("Bearer "):
            token = token[7:]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # print("payload:", payload)
        email = payload.get("sub")
        exp = payload.get("exp")
        # print(datetime.utcfromtimestamp(exp), datetime.utcnow())
        if datetime.utcfromtimestamp(exp) <= datetime.utcnow():
        # if exp <= datetime.utcnow.timestamp():
            raise HTTPException(status_code=401, detail="Token expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return storage.get_user(Client, email)

@app.get("/user/gymes")
async def home(request: Request):
    return templates.TemplateResponse(
        "userhome.html",
        {
            "request": request,
            "cities": storage.all_list(City),
            "amenities": storage.all_list(Amenity),
            "count": storage.pages_count(Gym),
            "price_range": storage.get_min_max_price()
        }
    )

@app.get("/tp")
async def tp(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "cities": storage.all_list(City),
            "amenities": storage.all_list(Amenity),
            "count": storage.pages_count(Gym)
        }
    )

# @app.post("/paypal_payment")
# async def process_paypal_payment(price: float = Form(...), duration: str = Form(...)):
#     payment = paypalrestsdk.Payment({
#         "intent": "sale",
#         "payer": {"payment_method": "paypal"},
#         "transactions": [{
#             "amount": {"total": price, "currency": "USD"},
#             "description": "Gym subscription payment"
#         }],
#         "redirect_urls": {
#             "return_url": "http://0.0.0.0:5000/paypal_success",
#             "cancel_url": "https://www.youtube.com"
#         }
#     })
#     if payment.create():
#         print("pay", payment)
#         return RedirectResponse(url=payment.links[1].href)
#     else:
#         raise HTTPException(status_code=400, detail="Payment creation failed")
    
@app.post("/paypal_payment")
async def process_paypal_payment(client_id: str = Form(...),
                                 gym_id: str = Form(...),
                                 price: float = Form(...),
                                 duration: str = Form(...)):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "transactions": [{
            "amount": {"total": price, "currency": "USD"},
            "description": "Gym subscription payment"
        }],
        "redirect_urls": {
            "return_url": "http://0.0.0.0:5000/paypal_success"+f"?client_id={client_id}&gym_id={gym_id}",
            "cancel_url": "https://www.youtube.com"
        },
    })
    if payment.create():
        print("pay", payment)
        return RedirectResponse(url=payment.links[1].href)
    else:
        raise HTTPException(status_code=400, detail="Payment creation failed")

@app.get("/paypal_success")
async def paypal_success(request: Request, client_id: str = Query(...), gym_id: str = Query(...)):
    payment_id = request.query_params.get('paymentId')
    payer_id = request.query_params.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)
    print("pay2", payment)
    if payment.execute({"payer_id": payer_id}):
        # Payment successful, store payment details in the database
        # Update user's subscription details
        enrolment_details = {
            "payment_id": payment_id,
            "client_id": client_id,
            "gym_id": gym_id,
            # "price": payment.transactions[0].amount.total,
            "from_date": datetime.utcnow(),
            "to_date": datetime.utcnow()+relativedelta(months=1)
        }
        new_enroll = EnrolClient(**enrolment_details)
        new_enroll.save()
        return templates.TemplateResponse(
            "success.html",
            {
                "request": request,
            }
        )
    else:
        raise HTTPException(status_code=400, detail="Payment execution failed")



@app.get("/user/history")
async def history(request: Request):
    return templates.TemplateResponse(
        "history.html",
        {
            "request": request,
        }
    )