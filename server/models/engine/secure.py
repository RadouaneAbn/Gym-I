from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from fastapi import Form

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="client/user/login")



def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)
