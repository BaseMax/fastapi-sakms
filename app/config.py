from pydantic import BaseModel
import os


class Settings(BaseModel):
    DB_URL: str = os.getenv(
        "DB_URL",
        "mysql+pymysql://root:password@127.0.0.1:3306/sakms"
    )
    JWT_SECRET: str = os.getenv("JWT_SECRET", "CHANGE_ME_SUPER_SECRET")
    JWT_ALGO: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24


settings = Settings()
