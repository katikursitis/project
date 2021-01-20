from flask import Flask, request
import src.models.dal as db
import src.models.users as user_model

app = Flask(__name__)

db.connect()


@app.route('/users/<user_id>', methods=['POST'])
def get_content(user_id):
    try:
        data = request.json
        if not data or not data['user_name']:
            return {'error': 'Bad request'}, 500

        user_model.save(user_id, data['user_name'])
        return {'status': 'OK', 'user_added': data['user_name']}, 200
    except Exception as e:
        return {'status': 'error', 'reason': str(e)}, 500


@app.errorhandler(404)
def not_found(e):
    return {'error': 'Not found'}, 404


app.run(host='127.0.0.1', debug=True, port=5000)
