from pydantic import BaseModel as BM
from typing import Optional
from fastapi import UploadFile, Form

class ClientModel(BM):
    first_name: str = Form(...)
    last_name: str = Form(...)
    email: str = Form(...)
    password: str = Form(...)
    # file_upload: UploadFile = None

class ClientModelPUT(BM):
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class ClientModelPWD(BM):
    old_password: str
    new_password: str

class EmailCheck(BM):
    email: str

class ClientLogin(BM):
    email: str
    password: str