from database.database import Session
from database.models.user_model import User


class UserController():
    def __init__(self):
        self.session = Session()

    def create_user(self, chat_id: int, name: str):
        db_user = User(chat_id=chat_id, name=name)
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)

        return db_user

    def get_user(self, user_id: int) -> User:
        user = self.session.query(User).filter(User.id == user_id).first()

        if not user:
            raise ValueError("User not found")
        
        return user

    def delete_user(self, user_id: int) -> None:
        db_user = self.session.query(User).filter(User.id == user_id).first()

        if not db_user:
            raise ValueError("User not found")

        self.session.delete(db_user)
        self.session.commit()

        return db_user