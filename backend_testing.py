import requests
import db_connector as db

db.connect()

try:
    user_id = '100'
    db.delete_user(user_id)  # Delete user_id for testing
    user_name = 'david'
    post_res = requests.post('http://127.0.0.1:5000/users/'+user_id, json={"user_name": user_name})
    if not post_res.status_code == 200:
        raise Exception("test failed")
    get_res = requests.get('http://127.0.0.1:5000/users/'+user_id)
    if not get_res.status_code == 200 or not get_res.json()['user_name'] == user_name:
        raise Exception("test failed")
    user_data = db.get_user(user_id)
    if not user_data or not user_data['user_name']:
        raise Exception("test failed")
    print("test success")
except Exception as e:
    print(e)



