import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

chrome_options = webdriver.ChromeOptions()
download_dir = os.path.abspath('./sample_folder/downloads')
prefs = {
    "download.default_directory": download_dir
}
chrome_options.add_experimental_option(name="prefs", value=prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/download")
time.sleep(3)
elements = driver.find_elements("xpath", "//div[@class='example']//a")
for element in elements:
    element.click()
time.sleep(3)