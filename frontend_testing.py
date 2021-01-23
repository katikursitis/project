from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chrome_driver = webdriver.Chrome(executable_path="/Users/Katya/Downloads/chromedriver", )


try:
    chrome_driver.get("http://127.0.0.1:5001/users/get_user_data/1")
    chrome_driver.implicitly_wait(3)
    user_element = chrome_driver.find_element_by_id("user")
    print(user_element.text)
    chrome_driver.quit()
except NoSuchElementException:
    print('Element not found')
    chrome_driver.quit()



