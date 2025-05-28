from flask import Flask, request, jsonify
from models import db, User, Action, Data, Policy
from config import Config
from utils import classify_data, monitor_actions

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/classify', methods=['POST'])
def classify():
    """
    Классификация данных по уровню конфиденциальности.
    """
    data_content = request.json.get('content')
    classification = classify_data(data_content)
    return jsonify({'classification': classification})

@app.route('/monitor', methods=['POST'])
def monitor():
    """
    Мониторинг действий пользователей.
    """
    user_id = request.json.get('user_id')
    action_type = request.json.get('action_type')
    monitor_actions(user_id, action_type)
    return jsonify({'status': 'success'})

@app.route('/report', methods=['GET'])
def generate_report():
    """
    Формирование отчета о действиях пользователей.
    """
    actions = Action.query.all()
    report = [
        {
            "id": action.id,
            "user_id": action.user_id,
            "action_type": action.action_type,
            "timestamp": action.timestamp.isoformat()
        }
        for action in actions
    ]
    return jsonify(report)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создание таблиц в базе данных
    app.run(debug=True)
