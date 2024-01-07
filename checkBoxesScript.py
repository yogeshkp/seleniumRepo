from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/checkboxes")

checkOne = driver.find_element(By.XPATH, "//*[@id='checkboxes']/input[1]")


time.sleep(5)
checkOne.click()
time.sleep(5)
checkTwo = driver.find_element(By.XPATH, "//*[@id='checkboxes']/input[2]")
checkTwo.click()
time.sleep(5)
driver.close()