from pydantic import BaseModel as BM

class CityModel(BM):
    name: str