""" Gym router
"""

from fastapi import APIRouter
from server.models.gym import Gym
from server.models.amenity import Amenity
from server.models import storage
from fastapi import HTTPException
from server.api.schemas.all_schemas import GymModel, GymModelPUT


gym_router = APIRouter()


@gym_router.get("/gymes/")
async def get_gymes():
    """ return all gyms """
    return [gym.to_dict() for gym in storage.all(Gym).values()]


@gym_router.get("/gymes/{gym_id}")
async def get_gym(gym_id: str):
    """ return gym using its id """
    gym = storage.get(Gym, gym_id)
    if gym is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return gym.to_dict(True)


@gym_router.post("/gymes/")
async def create_gym(gym: GymModel):
    """ Endpoint responsible for creating a Gym instances """
    gym.amenities = [storage.get(Amenity, amenity_id)
                     for amenity_id in gym.amenities]
    new_gym = Gym(**gym.__dict__)
    new_gym.save()
    return {"detail": "Gym created successfully"}


@gym_router.put("/gymes/{gym_id}")
async def update_user(gym_id: str, gym: GymModelPUT):
    """ Update a gym using its id """
    ignore = ["id", "created_id", "updated_at",
              "city_id", "user_id", "location"]
    inst = storage.get(Gym, gym_id)
    if inst is None:
        raise HTTPException(status_code=404, detail="Not Found")

    for key, value in gym.__dict__.items():
        if key in ignore or not value:
            continue
        setattr(inst, key, value)
    inst.save()
    return {"detail": "Gym updated successfully"}


@gym_router.delete("/gymes/{gym_id}/")
async def delete_gym(gym_id: str):
    gym = storage.get(Gym, gym_id)
    if gym is None:
        raise HTTPException(status_code=404, detail="Not Found")
    storage.delete(gym)
    storage.save()
    return {"detail": "Gym deleted successfully"}
