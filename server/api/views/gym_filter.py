from fastapi import APIRouter
from server.models.gym import Gym
from server.models.amenity import Amenity
from server.models.city import City
from server.models import storage
from server.api.schemas.gym_schema import GymModel, GymModelPUT, GymAmenity
from math import ceil
from time import time

gym_filter = APIRouter()

@gym_filter.post("/gym_filter/")
async def get_gym_amenity(data: GymAmenity):
    # st = time()
    amenity_list = set(storage.get(Amenity, am_id) for am_id in data.amenity_ids)
    # end = time()
    # print(end - st)

    offset = (data.page - 1) * 12
    limit = offset + 12
    if data.city_ids:
        all_gymes = storage.gymes_in_cities(data.city_ids)
    else:
        all_gymes = storage.all_list(Gym)
    # end = time()
    # print(end - st)
    # if amenity_list:
    #     all_gymes = [gym for gym in all_gymes if all(
    #         [amenity in gym.amenities for amenity in amenity_list])]

    filtered_gymes = []
    for gym in all_gymes:
        if amenity_list.issubset(gym.amenities):
            filtered_gymes.append(gym)

    if filtered_gymes:
        all_gymes = filtered_gymes

    # end = time()
    # print(end - st)

    count = ceil(len(all_gymes) / 12)
    # end = time()
    # print(end - st)
    all_gymes = all_gymes[offset:limit]
    for gym in all_gymes:
        setattr(gym, "city_name", storage.get(City, gym.city_id).name)
    # end = time()
    # print(end - st)
    return {count: [gym.to_dict(pop=["amenities"]) for gym in all_gymes]}

