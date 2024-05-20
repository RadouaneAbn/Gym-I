""" authenticate function
"""
from fastapi import Header, HTTPException
from server.models import storage
from fastapi import HTTPException
from jose import JWTError, jwt
from server.models.client import Client
from os import getenv
from datetime import datetime
from dateutil.relativedelta import relativedelta
from starlette.status import HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED
from server.models.engine.secure import verify_password

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")


def create_access_token(info: dict):
    """ This function creates a JWT token """
    data = info.copy()
    expire = datetime.utcnow() + relativedelta(months=1)
    data.update({"exp": expire})
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def check_token(authorization: str = Header(None)):
    """ This function validates and checkes a JWT token """
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400,
                            detail="Authorization header missing or invalid")
    try:
        token = authorization[7:]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = storage.get_user(Client, email)
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")

    return user


def authenticate_user(email, password, cls=Client):
    """ This function validates a user using (email, password) """
    user = storage.get_user(cls, email)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Email does not exist")
    if not verify_password(password, user.password):
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED,
                            detail="Incorrect password")
    return user
