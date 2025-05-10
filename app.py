from flask import Flask, request, jsonify
from models import db, User, Action, Data, Policy, Category
from config import Config
from utils import classify_data, monitor_actions

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/classify', methods=['POST'])
def classify():
    data_content = request.json.get('content')
    classification = classify_data(data_content)
    return jsonify({'classification': classification})

@app.route('/monitor', methods=['POST'])
def monitor():
    user_id = request.json.get('user_id')
    action_type = request.json.get('action_type')
    monitor_actions(user_id, action_type)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)