from sqlalchemy.orm import Session
from ..models.user import User
from ..security import hash_password, verify_password, create_access_token


class AuthService:

    @staticmethod
    def register(db: Session, email: str, password: str) -> str:
        user = User(email=email, password_hash=hash_password(password))
        db.add(user)
        db.commit()
        return user.id

    @staticmethod
    def login(db: Session, email: str, password: str) -> str | None:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return None
        if not verify_password(password, user.password_hash):
            return None
        return create_access_token(user.id)
