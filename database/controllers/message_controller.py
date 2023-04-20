from typing import List
from database.database import Session
from database.models.message_model import Message


class MessageController():
    def __init__(self):
        self.session = Session()

    def get_all_messages(self) -> List[Message]:
        messages = self.session.query(Message).all()

        return messages

    def get_messages(self, user_id: int):
        messages = self.session.query(Message).filter(Message.recipient_id == user_id).all()
        return messages if messages else []

    def create_message(self, sender: int, recipient: int, body: str) -> Message:
        db_message = Message(sender_id=sender, recipient_id=recipient, body=body, is_anonymous=True)

        self.session.add(db_message)
        self.session.commit()
        self.session.refresh(db_message)
        
        return db_message