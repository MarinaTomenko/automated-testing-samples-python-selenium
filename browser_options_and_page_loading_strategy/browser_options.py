from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "eager"
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors")
#chrome_options.add_argument("--window-size=700,700")
#chrome_options.add_argument("--disable-cache")
service = Service(executable_path=ChromeDriverManager().install())


driver = webdriver.Chrome(service=service, options=chrome_options)

driver.set_window_size(1920, 1980)

start_time = time.time()
driver.get("https://whatismyipaddress.com/")
#driver.get("https://expired.badssl.com/")
end_time = time.time()
result = end_time - start_time
print(result)
time.sleep(3)