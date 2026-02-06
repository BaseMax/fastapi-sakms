from sqlalchemy.orm import Session
from ..models.api_key import ApiKey
from ..security import generate_api_key, hash_password


class KeyService:

    @staticmethod
    def create_key(db: Session, user_id: str):
        raw, prefix = generate_api_key()

        key = ApiKey(
            key_prefix=prefix,
            key_hash=hash_password(raw),
            user_id=user_id,
        )

        db.add(key)
        db.commit()

        return key.id, raw, prefix

    @staticmethod
    def list_keys(db: Session, user_id: str):
        return db.query(ApiKey).filter(ApiKey.user_id == user_id).all()

    @staticmethod
    def revoke_key(db: Session, key_id: str, user_id: str) -> bool:
        key = db.query(ApiKey).filter(
            ApiKey.id == key_id,
            ApiKey.user_id == user_id
        ).first()

        if not key:
            return False

        key.revoked = True
        db.commit()
        return True
