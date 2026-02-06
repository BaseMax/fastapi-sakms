from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from ..database import get_db
from ..config import settings
from ..services.key_service import KeyService
from ..schemas.api_key import ApiKeyCreateResponse, ApiKeyInfo

router = APIRouter(prefix="/keys", tags=["API Keys"])


def get_user_id(token: str) -> str:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGO]
        )
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.post("/", response_model=ApiKeyCreateResponse)
def create_key(token: str, db: Session = Depends(get_db)):
    user_id = get_user_id(token)
    key_id, raw, prefix = KeyService.create_key(db, user_id)
    return ApiKeyCreateResponse(id=key_id, api_key=raw, prefix=prefix)


@router.get("/", response_model=list[ApiKeyInfo])
def list_keys(token: str, db: Session = Depends(get_db)):
    user_id = get_user_id(token)
    keys = KeyService.list_keys(db, user_id)
    return [
        ApiKeyInfo(id=k.id, prefix=k.key_prefix, revoked=k.revoked)
        for k in keys
    ]


@router.post("/{key_id}/revoke")
def revoke(key_id: str, token: str, db: Session = Depends(get_db)):
    user_id = get_user_id(token)
    ok = KeyService.revoke_key(db, key_id, user_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"status": "revoked"}
