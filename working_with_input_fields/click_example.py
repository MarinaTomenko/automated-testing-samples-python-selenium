from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/ru")

login_button = driver.find_element("xpath", "//a[@id='login-desktop']")
login_button.click()

time.sleep(3)

email_field = driver.find_element("xpath", "//input[@id='login_email']")
email_field.send_keys("email@ya.ru")

print(email_field.get_attribute("value"))
print(email_field.get_attribute("maxlength"))
time.sleep(3)
email_field.clear()
email_field.send_keys("AAAAAAAA")
time.sleep(3)