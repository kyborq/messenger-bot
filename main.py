from database.controllers.user_controller import UserController
from database.controllers.message_controller import MessageController
from database.init_database import create_tables


# Инициализируем базу данных
create_tables()


# Запускаем приложение
if __name__ == "__main__":
    user_controller = UserController()
    mail_controller = MessageController()
    
    u1 = user_controller.create_user(122, "Жужа")
    u1 = user_controller.create_user(123, "Игорь")
    u2 = user_controller.create_user(124, "Ваня")

    m1 = mail_controller.create_message(1, 2, "Привет!")
    m1 = mail_controller.create_message(3, 2, "Как дела?")
    ms1 = mail_controller.get_messages(2)

    print("App created!")
    print(ms1)