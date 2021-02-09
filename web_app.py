import os
import signal
from flask import Flask
import db_connector as db

app = Flask(__name__)

# connect to db
db.connect()


@app.route('/users/get_user_data/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user_data = db.get_user(user_id)
        if not user_data:
            return "<H1 id='error'>no such user:" + user_id + "</H1>", 500
        return "<H1 id='user'>" + user_data['user_name'] + "</H1>", 200
    except Exception as e:
        print(e)
        return "<H1 id='error'>Internal error</H1>", 500


@app.route('/stop_server')
def stop_server():
    db.close_connection()
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped'


@app.errorhandler(404)
def not_found(e):
    print(e)
    return "<H1 id='error'>Not found</H1>", 404


app.run(host='127.0.0.1', debug=True, port=5001)
