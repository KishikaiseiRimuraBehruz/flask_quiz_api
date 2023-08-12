from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String)
    email = db.Columnd(db.String)
    phone_number = db.Colmn(db.String,
                            unique=True)

class Leaders(db.Model):
    __tablename__ = 'Leaders'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    user_id = db.Column(db.Integer, db.Foreignkey('users.id'))
    level = db.Column(db.Integer,
                      nullable=False)
    score = db.Column(db.Integer)

    # сколько ForeignKey и столько user_fk = db.relationship(User) напишим
    user_fk = db.relationship(User)


# Таблица вопросов
class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer,
                   primery_key=True,
                   autoincrement=True)
    main_text = db.Column(db.String)
    variant_1 = db.Column(db.String,
                          nullable=False)
    variant_2 = db.Column(db.String,
                          nullable=False)
    variant_3 = db.Column(db.String)
    variant_4 = db.Column(db.String)
    correct_answer = db.Column(db.Integer,
                               nullable=False)
    level = db.Column(db.Integer,
                      nullable=False)

# Таблица ползователя ответов на вопросы
class UserAnswer(db.Model):
    __tablename__ = 'user_answer'
    id = db.Column(db.Integer,
                   primery_key=True,
                   autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'),
                            nullable=False)
    user_answer = db.Column(db.Integer,
                            nullable=False)
    correctness = db.Column(db.Boolean,
                            default=False)
    user_fk = db.relationship(User)
    question_fk = db.relationship(Question)
