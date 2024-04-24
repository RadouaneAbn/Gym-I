from pydantic import BaseModel as BM
from typing import Optional

class OwnerModel(BM):
    first_name: str
    last_name: str
    email: str
    password: str

class OwnerModelPUT(BM):
    first_name: Optional[str]
    last_name: Optional[str]

class OwnerModelPWD(BM):
    old_password: str
    new_password: str