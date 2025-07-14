from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://the-internet.herokuapp.com/status_codes")

status_code_links = driver.find_elements(By.XPATH, "//div[@class='example']//ul//a")
for link in status_code_links:
    link_text = link.text
    print(f"Click on the link: {link_text}")
    link.click()

    time.sleep(3)

    current_url = driver.current_url
    print(f"Current URL: {current_url}")

    driver.back()
    print("Returned to the home page")
    print("-" * 50)
