from pydantic import BaseModel
from typing import Optional

class CityModel(BaseModel):
    name: str

class AmenityModel(BaseModel):
    name: str

class GymModel(BaseModel):
    name: str
    city_id: str
    owner_id: str
    location: str
    description: str
    price_by_month: int
    price_by_year: Optional[int]
    amenities: list
    link: list

class ReviewModel(BaseModel):
    gym_id: str
    client_id: str
    text: str