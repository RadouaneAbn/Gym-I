from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    """ This function compares a hashed password with a password """
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password):
    """ This function hashes a password """
    return pwd_context.hash(password)
