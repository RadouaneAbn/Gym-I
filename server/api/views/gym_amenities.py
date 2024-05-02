from fastapi import APIRouter
from server.models.gym import Gym
from server.models.amenity import Amenity
from server.models import storage
from server.api.schemas.gym_schema import GymModel, GymModelPUT, GymAmenity

gym_amenity_router = APIRouter()

@gym_amenity_router.post("/gym_filter/")
async def get_gym_amenity(data: GymAmenity):
    amenity_list = [storage.get(Amenity, am_id) for am_id in data.amenity_ids]

    if data.city_ids:
        all_gymes = storage.gymes_in_cities(data.city_ids)
    else:
        all_gymes = storage.all_list(Gym)

    if amenity_list:
        all_gymes = [gym for gym in all_gymes if all(
            [amenity in gym.amenities for amenity in amenity_list])]

    return {f"{len(all_gymes)}": list(
        map(lambda x: x.to_dict(pop=["amenities"]), all_gymes))}

