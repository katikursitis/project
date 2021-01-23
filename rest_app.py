from flask import Flask, request
import db_connector as db

app = Flask(__name__)

# connect to db
db.connect()


@app.route('/users/<user_id>', methods=['POST'])
def create_user(user_id):
    try:
        data = request.json
        if not data or not data['user_name']:
            return {'error': 'Bad request'}, 500

        db.create_user(user_id, data['user_name'])
        return {'status': 'OK', 'user_added': data['user_name']}, 200
    except Exception as e:
        print(e)
        return {'status': 'error', 'reason': str(e)}, 500


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user_data = db.get_user(user_id)
        if not user_data:
            return {'status': 'error', 'reason': 'no such id'}, 500
        return {'status': 'OK', 'user_name': user_data['user_name']}, 200
    except Exception as e:
        print(e)
        return {'status': 'error', 'reason': 'Internal error'}, 500


@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.json
        if not data or not data['user_name']:
            return {'error': 'Bad request'}, 500

        db.update_user_name(user_id, data['user_name'])
        user_data = db.get_user(user_id)
        if not user_data:
            return {'status': 'error', 'reason': 'no such id'}, 500
        return {'status': 'OK', 'user_updated': user_data['user_name']}, 200
    except Exception as e:
        print(e)
        return {'status': 'error', 'reason': 'Internal error'}, 500


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        result = db.delete_user(user_id)
        if not result:
            return {'status': 'error', 'reason': 'no such id'}, 500
        return {'status': 'OK', 'user_deleted': user_id}, 200
    except Exception as e:
        print(e)
        return {'status': 'error', 'reason': 'Internal error'}, 500


@app.errorhandler(404)
def not_found(e):
    print(e)
    return {'error': 'Not found'}, 404


app.run(host='127.0.0.1', debug=True, port=5000)
