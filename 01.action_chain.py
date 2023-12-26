import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# create web driver instance
driver = webdriver.Chrome()
url = "file:///" + "home/my/Desktop/test/selenium-scripts/index.html"

driver.get(url)
username_link = driver.find_element(By.XPATH,"//input[@name='username']")

time.sleep(3)
username_link.send_keys("hello username")
password_link  = driver.find_element(By.XPATH, "//input[@name= 'password']")
time.sleep(3)
password_link.send_keys("password")



submit_link = driver.find_element(By.XPATH, "//input[@name = 'continue']")
submit_link.send_keys(Keys.ENTER)




time.sleep(5)
# action = ActionChains(driver)
# action.click(on_element=new_link)
# action.perform()
# # new_link.click()

driver.close()
