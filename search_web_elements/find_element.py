import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://ya.ru/")
time.sleep(2)
start_button = driver.find_element(By.CLASS_NAME, "headline__personal-enter")
time.sleep(2)
start_button.click()
time.sleep(5)