from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")

stepOne = driver.find_element(By.XPATH, "//*[@id='content']/ul/li[19]/a")
stepOne.click()

stepTwo = driver.find_element(By.XPATH, "//div[@id='menu']/ul/li[4]/a")
stepTwo.click()
print(stepTwo.get_attribute("href"))

time.sleep(5)

driver.close()