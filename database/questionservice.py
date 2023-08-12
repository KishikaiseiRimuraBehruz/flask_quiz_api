from models import Question, UserAnswer
from . import db
# funksiya dobavleniya voprosa - 7 parametrov
def add_questions(main_text, variant_1, variant_2, variant_3, variant_4, correct_answer, level):
    new_question = Question(main_text=main_text, variant_1=variant_1, variant_2=variant_2, variant_3=variant_3, variant_4=variant_4, correct_answer=correct_answer, level=level)
    db.session.add(new_question)
    db.session.commit()

# vivesti 20 voprosov
def questions_20(name_level):
    name = Question.query.filter_by(level=name_level).all()
    return name[:20]

# proverka otveta polzovatelya
def check_answers(q_id, user_answer):
    question_id = Question.query.filter_by(id=q_id).first()
    if question_id.correct_answer == user_answer:
       return True
    else:
        return False

