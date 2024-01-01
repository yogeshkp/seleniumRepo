from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/")

try:
    stepOne = driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[14]/a")
    stepOne.click()

    stepTwo = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/a[2]")
    stepTwo.click()

    stepThree = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/button")
    stepThree.click()
    # time.sleep(5)

    temp = (By.XPATH, "//*[@id='finish']/h4")
    element = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(temp))
    # input[name='login'][type='submit']
    print(element.text)

finally: 
    driver.quit()