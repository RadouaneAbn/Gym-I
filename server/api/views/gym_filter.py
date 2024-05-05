from fastapi import APIRouter
from server.models.gym import Gym
from server.models.amenity import Amenity
from server.models.city import City
from server.models import storage
from server.api.schemas.gym_schema import GymModel, GymModelPUT, GymAmenity
from math import ceil
from time import time

gym_filter = APIRouter()

def get_gym_filter(amenity_ids, city_ids, page):
    amenity_list = set(storage.get(Amenity, am_id) for am_id in amenity_ids)
    offset = (page - 1) * 12
    limit = offset + 12
    if city_ids:
        all_gymes = storage.gymes_in_cities(city_ids)
    else:
        all_gymes = storage.all_list(Gym)

    filtered_gymes = []
    if amenity_list:
        for gym in all_gymes:
            if amenity_list.issubset(gym.amenities):
                filtered_gymes.append(gym)

    if filtered_gymes:
        all_gymes = filtered_gymes

    count = ceil(len(all_gymes) / 12)

    all_gymes = all_gymes[offset:limit]
    return count, all_gymes

def get_gymes(page):
    return storage.pages_count(Gym), storage.get_page(Gym, page)


@gym_filter.post("/gym_filter/")
async def get_gym_amenity(data: GymAmenity):
    # st = time()
    if data.amenity_ids or data.city_ids:
        count, all_gymes = get_gym_filter(data.amenity_ids, data.city_ids, data.page)
    else:
        count, all_gymes = get_gymes(data.page)
    # print(all_gymes)
    for gym in all_gymes:
        setattr(gym, "city_name", storage.get(City, gym.city_id).name)

    return {count: [gym.to_dict(pop=["amenities"]) for gym in all_gymes]}

