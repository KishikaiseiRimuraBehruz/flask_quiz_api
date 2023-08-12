from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# импорт всех функции из файлов для бд
from .leaderservice import *
from .questionservice import *
from .registerservice import *
