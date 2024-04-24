from pydantic import BaseModel as BM
from typing import Optional

class ClientModel(BM):
    first_name: str
    last_name: str
    email: str
    password: str

class ClientModelPUT(BM):
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class ClientModelPWD(BM):
    old_password: str
    new_password: str

