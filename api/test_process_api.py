from . import api_bp
from ..database import user_and_test_db, check_answers, add_questions
# URL для получение вопросов
@api_bp.route('/get-questions/<int:level>', methods=['GET'])
def get_questions(level: int):
    result = get_questions.db(level)

    return {'status': 1, 'questions': result}


#URL для проверки ответа пользователя
@api_bp.route('/check-answer/<int:question_id>/<int:user_answer>', methods=['POST'])
def check_answer(questions_id: int, user_answer: int):
    result = check_answers(questions_id, user_answer)

    if result:
        return {'status': 1}


    else:
        return {'status': 0}

#URL для заверщение и получение результатов теста
@api_bp.route('/done/<int:user_id>/<int:correct_answers>', methods=['POST'])
def commit_user_answers(user_id: int, correct_answers: int,level: int):
    result = user_and_test_db(user_id, correct_answers, level)

    return {'status': 1, 'correct_answer': correct_answers, 'position_on_top': result}