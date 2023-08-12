from models import User
from . import db

# функция регистрации пользователя
def register_user_db(name, phone_number):
    # проверка ползователя на наличиее в базе
    checker = User.query.filter_by(phone_number=phone_number).first()

    # если есть ползователь
    if checker:
        return checker.id

    # Добовление данных в базу
    new_user = User(name=name, phone_number=phone_number)
    db.session.add(new_user)
    db.session.commit()

    return new_user.id

