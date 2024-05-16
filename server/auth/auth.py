from fastapi import Header, HTTPException
from server.models import storage
from fastapi import HTTPException
from jose import JWTError, jwt
from server.models.client import Client

SECRET_KEY = "4f0e2935cdf27d24222357163158cb6d481bc67c5e15c2eaa1c5982ecf3e80b1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
def check_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="Authorization header missing or invalid")
    try:
        token = authorization[7:]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # print("payload:", payload)
        email = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = storage.get_user(Client, email)
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")

    return user
