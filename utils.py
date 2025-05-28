from models import Action, db

def classify_data(data_content):
    """
    Простая классификация данных по уровню конфиденциальности.
    """
    if 'конфиденциальная' in data_content.lower():
        return 'confidential'
    elif 'личная' in data_content.lower():
        return 'personal'
    else:
        return 'public'

def monitor_actions(user_id, action_type):
    """
    Логирование действий пользователей.
    """
    action = Action(user_id=user_id, action_type=action_type)
    db.session.add(action)
    db.session.commit()
