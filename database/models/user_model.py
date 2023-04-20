from sqlalchemy import Column, Integer, String
from database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<User {self.chat_id}: {self.name}>"
