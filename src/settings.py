from passlib.context import CryptContext

from .types import Settings


SETTINGS = Settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
