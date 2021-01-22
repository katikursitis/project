import requests
import db_connector as db

db.connect()

try:
    user_id = '100'
    db.delete_user(user_id)  # Delete user_id for testing
    user_name = 'david'
    post_res = requests.post('http://127.0.0.1:5000/users/'+user_id, json={"user_name": user_name})
    get_res = requests.get('http://127.0.0.1:5000/users/'+user_id)
    user_data = db.get_user(user_id)
    if post_res.status_code == 200 and get_res.status_code == 200 and user_data['user_name'] == user_name:
        print("Success")
except Exception as e:
    print(e)



