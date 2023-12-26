from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")

assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
time.sleep(3)
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.ENTER)

time.sleep(10)
driver.close()