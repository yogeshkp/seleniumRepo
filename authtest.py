from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

service = Service("/home/my/Desktop/test/seleniumRepo/chromedriver")

test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

options = Options()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.XPATH, "//*[@id='user-name']")
username.send_keys("standard_user")


passwd = driver.find_element(By.XPATH, "//*[@id='password']")
passwd.send_keys("secret_sauce")

click_login = driver.find_element(By.XPATH, "//*[@id='login-button']")
click_login.click()
print("login ran successfully")


# ham = driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']")
# ham.click()
# print("ham clicked")

# logout = driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']")
# logout.click()
# print("loggedout successfully")

# listitems = driver.find_elements(By.CLASS_NAME,"inventory_item_name ")
# listprice = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
listitems = driver.find_elements(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
# print(listitems)
# for no,item,des,price in zip(range(1,len(listitems)+1),listitems,listDesc,listprice):
#     print(no,item.text,des.text, price.text)
# print(type(listitems))
# print(listitems.get_attribute("value"))
for item in listitems:
    print(item.text)

# name="add-to-cart-sauce-labs-backpack"
time.sleep(10)
driver.close()

# //*[@id='inventory_container']/div/div[1]