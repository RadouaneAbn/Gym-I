#!/usr/bin/python3
""" Cities end points """
from fastapi import APIRouter
from server.models.city import City
from server.models import storage
from fastapi import HTTPException
from server.api.schemas.all_schemas import CityModel
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

city_router = APIRouter()


@city_router.get("/cities/")
async def get_cities():
    """ Return all cities """
    return [city.to_dict() for city in storage.all(
        City).values()], HTTP_200_OK


@city_router.get("/cities/{city_id}")
async def get_city(city_id: str):
    """ Return a city by id """
    city = storage.get(City, city_id)
    if city is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return city.to_dict(), HTTP_200_OK


@city_router.post("/cities/")
async def create_city(city: CityModel):
    """ create a city """
    new_city = City(**city.__dict__)
    new_city.save()
    return {"detail": "City created successfully"}, HTTP_201_CREATED


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
    return {"detail": "City updated successfully"}, HTTP_200_OK


@city_router.delete("/cities/{city_id}/")
async def delete_city(city_id: str):
    city = storage.get(City, city_id)
    if city is None:
        raise HTTPException(status_code=404, detail="Not Found")
    storage.delete(city)
    storage.save()
    return {"detail": "City deleted successfully"}, HTTP_200_OK
