import requests
import db_connector as db
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import random

# connect to db
db.connect()

# get configuration from db
config = db.get_configurations('testing')
user_name = config['user_name']
rest_url = config['rest_gateway_url']
web_url = config['web_gateway_url']
browser = config['browser']

# start Chrome driver
web_browser = getattr(webdriver, browser)
chrome_driver = web_browser(executable_path="/Users/Katya/Downloads/chromedriver", )


try:
    while True:  # go throw loop while getting id already exist error
        user_id = str(random.randint(1, 100))  # generate random user_id
        post_res = requests.post(rest_url + user_id, json={"user_name": user_name})  # send request to create new user
        # check response code and response reason
        if not post_res.status_code == 200 and post_res.json()['reason'] == 'id already exists':
            continue  # generated id already exist in db, try again in loop
        # check if there are another error
        if not post_res.status_code == 200 and not post_res.json()['reason'] == 'id already exists':
            raise Exception("test failed")  # there are another error during creating new user, test failed
        else:
            break  # stop loop because user was created successfully

    get_res = requests.get(rest_url + user_id)  # send get request to get created user
    # check response code and response user_name
    if not get_res.status_code == 200 or not get_res.json()['user_name'] == user_name:
        # if the response code is not 200 or user_name is different test failed
        raise Exception("test failed")
    user_data = db.get_user(user_id)  # get user from db by user_id
    # check the user from db
    if not user_data or not user_data['user_name'] or not user_data['user_name'] == user_name:
        raise Exception("test failed")
    chrome_driver.get(web_url + user_id)  # get web page of user data
    chrome_driver.implicitly_wait(3)  # wait until page is loading
    user_element = chrome_driver.find_element_by_id("user")  # find user element on page
    if not user_element.text == user_name:  # check text of element
        raise Exception("test failed")
    print("test success")
    chrome_driver.quit()
except NoSuchElementException:
    print('test failed')
except Exception as e:
    print(e)
finally:
    chrome_driver.quit()  # close driver
