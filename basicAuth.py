from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/")

