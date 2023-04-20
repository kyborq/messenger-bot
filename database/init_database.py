from database.database import Base, engine
from database.models.user_model import User
from database.models.message_model import Message


def create_tables():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
