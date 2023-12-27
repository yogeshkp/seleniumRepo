from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/?ref=hackernoon.com")

element = driver.find_element(By.XPATH, "//*[@id='content']/ul/li[1]/a")
element.click()


print("link is clicked")
time.sleep(5)
driver.close()

