from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import os
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/ru/login")

login_field = driver.find_element("xpath", "//input[@id='login_email']")
login_field.send_keys("myEmail@yandex.ru")

password_field = driver.find_element("xpath", "//input[@id='password']")
password_field.send_keys("password")

agree_checkbox = driver.find_element("xpath", "//input[@name='rememberme']")
agree_checkbox.click()

submit_button = driver.find_element("xpath", "//button[@id='loginformsubmit']")
submit_button.click()

driver.get("https://www.freeconferencecall.com/profile/settings?tab=wall-editor")
time.sleep(5)
upload_field = submit_button = driver.find_element("xpath", "//input[@type='file']")
upload_field.send_keys(f"{os.getcwd()}\downloads\91231.jpg")
time.sleep(5)