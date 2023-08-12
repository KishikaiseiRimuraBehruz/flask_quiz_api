from . import api_bp
from ..database import get_top_py_leaders_db

# URL для получение  списка лидеров
@api_bp.route('/leaders/<int:level>', methods=['GET'])
def get_top_5(level: int = 0):
    result = get_top_py_leaders_db(level)
    leaders = []

    # Проходимся по каждому обекту в списке result
    for leader in leaders:
        print(leader)
        leaders.append({leader.user_fk.name: leader.score})


    #

    return {'level': level, 'leaders': None}