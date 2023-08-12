from . import db
from models import Leaders, UserAnswer


# Запись результата текущего пользователя
def user_and_test_db(user_id, correct_answers, level):
    exact_user_score = Leaders.query.filter_by(user_id=user_id, level=level).first()


    # проверить есть ли что то внутри базы
    if exact_user_score:
        # к старым очкам добавить текущие
        exact_user_score.score += correct_answers
        db.session.commit()
    # а если не было пользователя
    else:
        # создаем запись в базе данных
        new_leader_data = Leaders(user_id=user_id, level=level, score=correct_answers)

        db.session.add(new_leader_data)
        db.session.commit()

    return True

# Вывод лидеров из конкрутных уровней
def get_top_py_leaders_db(level):
    exact_level_leaders = Leaders.query.filter_by\
        (level=level).order_by(Leaders.score.desc()).all()
    return  exact_level_leaders[:6]


# Запись каждого ответа ползователя
def add_user_answer_db(user_id, q_id, user_answer, correctness):
    new_answer = UserAnswer(user_id=user_id,
                            question_id=q_id,
                            user_answer=user_answer,
                            correctness=correctness
    )

    db.session.add(new_answer)
    db.session.commit()

    return True