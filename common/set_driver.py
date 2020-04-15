import os
from selenium import webdriver

def set_driver():
    current = os.path.dirname(__file__)
    chrome_webdrive_path = os.path.join(current, '../webdriver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=chrome_webdrive_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://127.0.0.1/zentao/my')
    return driver