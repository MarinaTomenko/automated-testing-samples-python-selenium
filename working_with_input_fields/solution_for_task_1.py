from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")

username_field = driver.find_element("xpath", "//input[@id='userName']")
username_field.clear()
username_field.send_keys("Marina Tomenko")

useremail_field = driver.find_element("xpath", "//input[@id='userEmail']")
useremail_field.clear()
useremail_field.send_keys("myEmail@yandex.ru")

currentaddress_field = driver.find_element("xpath", "//textarea[@id='currentAddress']")
currentaddress_field.clear()
currentaddress_field.send_keys("Russia")

permanentaddress_field = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
permanentaddress_field.clear()
permanentaddress_field.send_keys("Russia")

username_value = username_field.get_attribute("value")
email_value = useremail_field.get_attribute("value")
currentaddress_value = currentaddress_field.get_attribute("value")
permanentaddress_value = permanentaddress_field.get_attribute("value")

print("Current username field:" , username_value)
assert username_value == "Marina Tomenko", "incorrect username."

print("Current email field:" , email_value)
assert email_value == "myEmail@yandex.ru", "incorrect email."

print("Current first address field:" , currentaddress_value)
assert currentaddress_value == "Russia", "incorrect current address."

print("Current second address field:" , permanentaddress_value)
assert permanentaddress_value == "Russia", "incorrect permanent address."