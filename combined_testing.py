import requests
import db_connector as db
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

db.connect()
chrome_driver = webdriver.Chrome(executable_path="/Users/Katya/Downloads/chromedriver", )


try:
    user_id = '100'
    db.delete_user(user_id)  # Delete user_id for testing
    user_name = 'katya'
    post_res = requests.post('http://127.0.0.1:5000/users/'+user_id, json={"user_name": user_name})
    if not post_res.status_code == 200:
        raise Exception("test failed")
    get_res = requests.get('http://127.0.0.1:5000/users/'+user_id)
    if not get_res.status_code == 200 or not get_res.json()['user_name'] == user_name:
        raise Exception("test failed")
    user_data = db.get_user(user_id)
    if not user_data or not user_data['user_name']:
        raise Exception("test failed")
    chrome_driver.get("http://127.0.0.1:5001/users/get_user_data/" + user_id)
    chrome_driver.implicitly_wait(3)
    user_element = chrome_driver.find_element_by_id("user")
    if not user_element.text == user_name:
        raise Exception("test failed")
    print("test success")
    chrome_driver.quit()
except NoSuchElementException:
    print('test failed')
except Exception as e:
    print(e)
    chrome_driver.quit()
