import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

url = driver.current_url
print("Page URL:" , url)
assert url == "https://www.wikipedia.org/", "Error in URL, opened the wrong page."

current_title = driver.title
print("Current title:" , current_title)
assert current_title == "Wikipedia", "Incorrect page title."


print(driver.page_source)
time.sleep(3)

