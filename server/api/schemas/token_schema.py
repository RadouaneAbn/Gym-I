from pydantic import BaseModel as BM
from typing import Optional

class Token(BM):
    access_token: str
    token_type: str

class TokenData(BM):
    token: str = None
