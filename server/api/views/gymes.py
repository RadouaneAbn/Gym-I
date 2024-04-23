from fastapi import APIRouter
from models.gym import Gym
from models import storage
from fastapi import FastAPI, HTTPException
from api.schemas.gym_schema import GymModel, GymModelPUT, GymModelUserPUT, GymModelAmenity

gym_router = APIRouter()

@gym_router.get("/gymes/")
async def get_gymes():
    return [gym.to_dict() for gym in storage.all(Gym).values()]

@gym_router.get("/gymes/{gym_id}")
async def get_gym(gym_id: str):
    gym = storage.get(Gym, gym_id)
    if gym is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return gym.to_dict(True)

@gym_router.post("/gymes/")
async def create_gym(gym: GymModel):
    new_gym = Gym(**gym.__dict__)
    new_gym.save() 

@gym_router.put("/gymes/{gym_id}")
async def update_user(gym_id: str, gym: GymModelPUT):
    ignore = ["id", "created_id", "updated_at", "city_id", "user_id", "location"]
    inst = storage.get(Gym, gym_id)
    if inst is None:
        raise HTTPException(status_code=404, detail="Not Found")

    for key, value in gym.__dict__.items():
        if key in ignore or not value:
            continue
        setattr(inst, key, value)
    inst.save()

@gym_router.delete("/gymes/{gym_id}/")
async def delete_gym(gym_id: str):
    gym = storage.get(Gym, gym_id)
    if gym is None:
        raise HTTPException(status_code=404, detail="Not Found")
    storage.delete(gym)
    storage.save()
