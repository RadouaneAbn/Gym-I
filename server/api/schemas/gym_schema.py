from pydantic import BaseModel as BM
from typing import Optional

class GymModel(BM):
    name: str
    city_id: str
    user_id: str
    location: str
    description: str
    price_by_month: float
    price_by_year: Optional[float]
    amenities: list
    links: Optional[list]

class GymModelPUT(BM):
    name: Optional[str]
    description: Optional[str]
    price_by_month: Optional[float]
    price_by_year: Optional[float]
    amenities: Optional[list]
    links: Optional[list]

# for future use if the onwer wanted to change the ownership of teh gym
# class GymModelUserPUT(BM):
#     user_id: str

class GymModelAmenity(BM):
    city_id: str = None
    amenities: list = None