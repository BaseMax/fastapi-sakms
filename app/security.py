from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from secrets import token_urlsafe
from .config import settings


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)


def create_access_token(subject: str) -> str:
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGO)


def generate_api_key() -> tuple[str, str]:
    raw = token_urlsafe(32)
    prefix = raw[:8]
    return raw, prefix
