import requests
import db_connector as db
import random

db.connect()
config = db.get_configurations('testing')
user_name = config['user_name']
rest_url = config['rest_gateway_url']

try:
    while True:
        user_id = str(random.randint(1, 100))
        post_res = requests.post(rest_url + user_id, json={"user_name": user_name})
        if not post_res.status_code == 200 and post_res.json()['reason'] == 'id already exists':
            continue
        if not post_res.status_code == 200 and not post_res.json()['reason'] == 'id already exists':
            raise Exception("test failed")
        else:
            break

    get_res = requests.get(rest_url + user_id)
    if not get_res.status_code == 200 or not get_res.json()['user_name'] == user_name:
        raise Exception("test failed")
    user_data = db.get_user(user_id)
    if not user_data or not user_data['user_name']:
        raise Exception("test failed")
    print("test success")
except Exception as e:
    print(e)



