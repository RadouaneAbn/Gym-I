from pydantic import BaseModel as BM

class AmenityModel(BM):
    name: str