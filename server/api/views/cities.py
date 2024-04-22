#!/usr/bin/python3

from fastapi import APIRouter
from models.city import City
from models import storage
from fastapi import HTTPException
from api.schemas.city_schema import CityModel


city_router = APIRouter()

@city_router.get("/cities/")
async def get_cities():
    return [city.to_dict() for city in storage.all(City).values()]

@city_router.get("/cities/{city_id}")
async def get_city(city_id: str):
    city = storage.get(City, city_id)
    if city is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return city.to_dict()

@city_router.post("/cities/")
async def create_city(city: CityModel):
    new_city = City(**city.__dict__)
    new_city.save()

@city_router.put("/cities/{city_id}")
async def update_city(city_id: str, city: CityModel):
    ignore = ["id", "created_id", "updated_at"]
    inst = storage.get(City, city_id)
    if inst is None:
        raise HTTPException(status_code=404, detail="Not Found")
    
    for key, value in city.__dict__.items():
        if key in ignore or not value:
            continue
        setattr(inst, key, value)
    inst.save()

@city_router.delete("/cities/{city_id}/")
async def delete_city(city_id: str):
    city = storage.get(City, city_id)
    if city is None:
        raise HTTPException(status_code=404, detail="Not Found")
    storage.delete(city)
    storage.save()