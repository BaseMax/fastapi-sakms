from pydantic import BaseModel


class ApiKeyCreateResponse(BaseModel):
    id: str
    api_key: str
    prefix: str


class ApiKeyInfo(BaseModel):
    id: str
    prefix: str
    revoked: bool
