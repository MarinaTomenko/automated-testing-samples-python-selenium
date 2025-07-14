import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

driver.find_element("class name", "wikipedia-icon")
driver.find_element("id", "Wikipedia1_wikipedia-search-input")
driver.find_element("class name", "wikipedia-search-button")
driver.find_element("class name", "dropbtn")
time.sleep(5)