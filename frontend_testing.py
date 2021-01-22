from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chrome_driver = webdriver.Chrome(executable_path="/Users/Katya/Downloads/chromedriver", )

chrome_driver.get("http://127.0.0.1:5001/users/get_user_data/1")

try:
    chrome_driver.implicitly_wait(3)
    user_element = chrome_driver.find_element_by_id("user")
    print(user_element.text)
except NoSuchElementException:
    print('Element not found')


chrome_driver.quit()
