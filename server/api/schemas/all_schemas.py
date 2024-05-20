from pydantic import BaseModel as BM
from typing import Optional
from fastapi import Form


class AmenityModel(BM):
    name: str


class CityModel(BM):
    name: str


class ClientModel(BM):
    first_name: str = Form(...)
    last_name: str = Form(...)
    email: str = Form(...)
    password: str = Form(...)


class ClientModelPUT(BM):
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class ClientModelPWD(BM):
    old_password: str
    new_password: str


class EmailCheck(BM):
    email: str


class ClientLogin(BM):
    email: str
    password: str


class GetEnroleAll(BM):
    client_id: str


class EnrolData(BM):
    payment_id: str
    gym_id: str
    date: str
    months: str


class GymModel(BM):
    name: str
    city_id: str
    owner_id: str
    location: str
    description: str
    price_by_month: float = 0
    price_by_year: float = 0
    profile_picture: str
    amenities: list = []
    links: list = []


class GymModelPUT(BM):
    name: Optional[str]
    description: Optional[str]
    price_by_month: Optional[float]
    price_by_year: Optional[float]
    amenities: Optional[list]
    links: Optional[list]


class GymAmenity(BM):
    price_range: dict = {}
    search_text: str = ""
    city_ids: list = []
    amenity_ids: list = []
    page: int = 1


class GymSearch(BM):
    name: str = None


class OwnerModel(BM):
    first_name: str
    last_name: str
    email: str
    password: str


class OwnerModelPUT(BM):
    first_name: Optional[str]
    last_name: Optional[str]


class OwnerModelPWD(BM):
    old_password: str
    new_password: str


class ReviewModel(BM):
    client_id: str
    text: str


class ReviewModel(BM):
    text: str


class Token(BM):
    access_token: str
    token_type: str


class TokenData(BM):
    token: str = None
