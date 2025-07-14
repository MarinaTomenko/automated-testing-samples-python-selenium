from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)
driver.implicitly_wait(30)
driver.get("https://omayo.blogspot.com/")

DISAPPEARING_TEXT = ("xpath", "//div[@id='hidediv']")
wait.until(EC.invisibility_of_element_located(DISAPPEARING_TEXT))
print("The text has disappeared")

DELAYED_TEXT = ("xpath", "//div[@id='delayedText']")
wait.until(EC.visibility_of_element_located(DELAYED_TEXT))
print("The text appeared")

ENABLE_BUTTON = ("xpath", "//input[@id='timerButton']")
wait.until(EC.element_to_be_clickable(ENABLE_BUTTON))
print("Button Button3 has become clickable")

TRY_IT_BUTTON = ("xpath", "//button[text()='Try it']")
DISABLED_BUTTON = ("xpath", "//button[@id='myBtn']")
driver.find_element(*TRY_IT_BUTTON).click()
#wait.until(EC.element_to_be_clickable(DISABLED_BUTTON))
wait.until(lambda driver: not driver.find_element(*DISABLED_BUTTON).is_enabled())
print("Button My Button became disabled after clicking")
