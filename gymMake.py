from server.models.amenity import Amenity
from server.models.city import City
from server.models.client import Client
from server.models.gym import Gym
from server.models.owner import Owner
from server.models.review import Review
from server.models import storage

amenity = "Security cameras"
city = "Safi"
owner = {"first_name": "test", "last_name": "test", "email": "red@gmail.com", "password": "1234"}
gymes = []

city = City(name=city)
amenity = Amenity(name=amenity)
owner = Owner(**owner)

city.save()
amenity.save()
owner.save()

for i in range(1000):
    gym = Gym(name="test", owner_id=owner.id, city_id=city.id, location="", description="rewFFEEFeff", price_by_month=50, amenities = [amenity], profile_picture="")
    gym.save()
    gymes.append(gym)


try:
    n = input('click to continue')
    raise Exception
except Exception:
    for gym in gymes:
        gym.delete()
    owner.delete()
    city.delete()
    owner.delete()
