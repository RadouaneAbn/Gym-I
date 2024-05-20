#!/usr/bin/python3
""" Amenities end points """
from fastapi import APIRouter
from server.models.amenity import Amenity
from server.models import storage
from fastapi import HTTPException
from server.api.schemas.all_schemas import AmenityModel
amenity_router = APIRouter()


@amenity_router.get("/amenities/")
async def get_amenities():
    """ Return all amenities """
    return [amenity.to_dict() for amenity in storage.all(
        Amenity).values()]


@amenity_router.get("/amenities/{amenity_id}")
async def get_amenity(amenity_id: str):
    """ Return an Amenity instance if found or raise 404 """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return amenity.to_dict()


@amenity_router.post("/amenities/")
async def create_amenity(amenity: AmenityModel):
    """ POST request to create an Amenity """
    new_amenity = Amenity(**amenity.__dict__)
    new_amenity.save()
    return {"detail": "amenity created successfully"}


@amenity_router.put("/amenities/{amenity_id}")
async def update_amenity(amenity_id: str, amenity: AmenityModel):
    """ PUT request to update an Amenity """
    ignore = ["id", "created_id", "updated_at"]
    inst = storage.get(Amenity, amenity_id)
    if inst is None:
        raise HTTPException(status_code=404, detail="Not Found")

    for key, value in amenity.__dict__.items():
        if key in ignore or not value:
            continue
        setattr(inst, key, value)
    inst.save()
    return {"detail": "amenity updated successfully"}


@amenity_router.delete("/amenities/{amenity_id}/")
async def delete_amenity(amenity_id: str):
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        raise HTTPException(status_code=404, detail="Not Found")
    storage.delete(amenity)
    storage.save()
    return {"detail": "amenity deleted successfully"}
