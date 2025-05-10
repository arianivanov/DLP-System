import pandas as pd

def classify_data(data_content):
    # Пример простой классификации данных
    if 'конфиденциальная' in data_content.lower():
        return 'confidential'
    elif 'личная' in data_content.lower():
        return 'personal'
    else:
        return 'public'

def monitor_actions(user_id, action_type):
    # Пример записи действия пользователя
    from models import Action, db
    action = Action(user_id=user_id, action_type=action_type)
    db.session.add(action)
    db.session.commit()