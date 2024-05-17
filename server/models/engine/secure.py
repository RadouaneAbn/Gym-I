from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="client/user/login")


def verify_password(plain_password, hashed_password):
    """ This function compares a hashed password with a password """
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password):
    """ This function hashes a password """
    return pwd_context.hash(password)
