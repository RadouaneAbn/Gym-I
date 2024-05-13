from fastapi import APIRouter
from server.models.gym import Gym
from server.models.amenity import Amenity
from server.models.city import City
from server.models import storage
from server.api.schemas.gym_schema import GymAmenity, GymSearch
from math import ceil

gym_filter = APIRouter()

def filter_by_amenity(gyms, amenity_list):
    filtered_gyms = []
    for gym in gyms:
        if amenity_list.issubset(gym.amenities):
            filtered_gyms.append(gym)
    return filtered_gyms

def get_gym_filter(search_text, amenity_ids, city_ids, page, price_range):
    amenity_list = set(storage.get(Amenity, am_id) for am_id in amenity_ids)
    offset = (page - 1) * 12
    limit = offset + 12
    if city_ids:
        all_gymes = storage.gymes_in_cities(city_ids, search_text)
    else:
        all_gymes = storage.all_list(Gym, search_text)
    
    if amenity_list:
        all_gymes = filter_by_amenity(all_gymes, amenity_list)

    if price_range:
        all_gymes = filter_by_price(all_gymes, price_range)

    count = ceil(len(all_gymes) / 12)

    all_gymes = all_gymes[offset:limit]
    return count, all_gymes

def get_gymes(page):
    return storage.pages_count(Gym), storage.get_page(Gym, page)

def filter_by_price(gyms, price_range):
    new_gyms = []
    for gym in gyms:
        if gym.price_by_month >= price_range["min"] and\
            gym.price_by_month <= price_range["max"]:
            new_gyms.append(gym)
    return new_gyms


@gym_filter.post("/gym_filter/")
async def get_gym_amenity(data: GymAmenity):
    count, all_gymes = get_gym_filter(data.search_text, data.amenity_ids,
                                        data.city_ids, data.page, data.price_range)

    for gym in all_gymes:
        setattr(gym, "city_name", storage.get(City, gym.city_id).name)

    return {count: [gym.to_dict(pop=["amenities"]) for gym in all_gymes]}

@gym_filter.post("/gym_search/")
async def gym_search(data: GymSearch):
    if not data.name:
        return []
    return storage.search(data.name)