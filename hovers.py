from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/")
stepOne = driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[25]/a")
stepOne.click()


action = ActionChains(driver)

username = list()

listOfElements = driver.find_element(By.XPATH,"//*[@id='content']/div")
print(listOfElements)
# stepTwo = driver.find_element(By.XPATH, "//*[@id='content']/div/div[1]")
# action.move_to_element(stepTwo)
# action.perform()


# print(stepTwo.text)
# element = EC.visibility_of_element_located()
driver.quit()