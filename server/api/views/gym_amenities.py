from fastapi import APIRouter
from models.gym import Gym
from models.amenity import Amenity
from models import storage
from fastapi import FastAPI, HTTPException
from api.schemas.gym_schema import GymModel, GymModelPUT, GymModelUserPUT, GymModelAmenity

gym_amenity_router = APIRouter()

@gym_amenity_router.post("/gymes/")
async def get_gym_amenity(amenity_ids: GymModelAmenity):
    amenities = amenity_ids.amenities
    amenity_list = []
    for amenity_id in amenities:
        instance = storage.get(Amenity, amenity_id)
        if not instance:
            print("Amenity not found " + amenity_id)
            continue
        amenity_list.append(instance)
    
    all_gymes = storage.all(Gym).values()

    if amenity_list:
        for gym in all_gymes:
            if not all(amenity in gym.amenities for amenity in amenity_list):
                all_gymes.pop(gym)

    return all_gymes

