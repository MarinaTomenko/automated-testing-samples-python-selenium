import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://vk.com/")
current_title_vk = driver.title
print("Current title:" , current_title_vk)

driver.get("https://ya.ru/")
current_title_ya = driver.title
print("Current title:" , current_title_ya)

driver.back()
assert current_title_vk == "ВКонтакте | Добро пожаловать", "Incorrect page title."
driver.refresh()

url = driver.current_url
print("URL страницы:" , url)
assert url == "https://vk.com/", "Error in URL, opened the wrong page."
driver.forward()
url = driver.current_url
print("URL страницы:" , url)
assert url == "https://ya.ru/", "Error in URL, opened the wrong page."

time.sleep(3)