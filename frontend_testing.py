from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import db_connector as db

# connect to db
db.connect()

# get configuration from db
config = db.get_configurations('testing')
web_url = config['web_gateway_url']
browser = config['browser']

# start Chrome driver
web_browser = getattr(webdriver, browser)
chrome_driver = web_browser(executable_path="/Users/Katya/Downloads/chromedriver", )

try:
    user_id = '1'
    chrome_driver.get(web_url + user_id)
    chrome_driver.implicitly_wait(3)
    user_element = chrome_driver.find_element_by_id("user")
    print(user_element.text)
    chrome_driver.quit()
except NoSuchElementException:
    print('Element not found')
finally:
    chrome_driver.quit()



