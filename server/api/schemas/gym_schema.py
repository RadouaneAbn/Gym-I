from pydantic import BaseModel as BM
from typing import Optional

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
    search_text: str = ""
    city_ids: list = []
    amenity_ids: list = []
    page: int = 1

class GymSearch(BM):
    name: str = None

# for future use if the onwer wanted to change the ownership of teh gym
# class GymModelUserPUT(BM):
#     owner_id: str
