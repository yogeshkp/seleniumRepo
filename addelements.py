from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button")
for i in range(5):
    element.send_keys(Keys.ENTER)
    print(str(i) + "new element added")

print(element.text)

time.sleep(10)
print("script ran successfully")

driver.close()