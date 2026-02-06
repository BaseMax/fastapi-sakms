from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from uuid import uuid4

from ..models.user import User
from ..security import hash_password, verify_password, create_access_token


class AuthService:

    @staticmethod
    def register(db: Session, email: str, password: str) -> str:
        existing = db.query(User).filter(User.email == email).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )

        user = User(
            id=str(uuid4()),
            email=email,
            password_hash=hash_password(password),
            is_active=True,
        )

        db.add(user)

        try:
            db.commit()
            db.refresh(user)
            return user.id

        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )

    @staticmethod
    def login(db: Session, email: str, password: str) -> str | None:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return None
        if not verify_password(password, user.password_hash):
            return None
        return create_access_token(user.id)
