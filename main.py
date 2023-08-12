from flask import Flask
from database import db

#создаем обьект к классу SQLAlchemy

app = Flask(__name__)

#　создаем крнфинурацию базы данныйх для проекта и указываем путь
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///project.db"
#регистрируем базу на проект
db.init_app(app)

