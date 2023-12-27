from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

service = Service("/home/my/Desktop/test/seleniumRepo/chromedriver")

test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

options = Options()

# options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
options.add_argument("--window-size=1920,1080")

options.add_argument(f'--user-agent={test_ua}')

options.add_argument('--no-sandbox')
options.add_argument("--disable-extensions")

test_driver = webdriver.Chrome(service=service, options=options)

solver = RecaptchaSolver(driver=test_driver)

test_driver.get('https://www.cubexo.keka.com')

# username = driver.find_element(By.NAME, "Email")
# driver.send_keys("yogesh.patel@cubexo.io")
# passwd= driver.find_element(By.NAME, "Password")
# driver.send_keys("enter passwrd")

recaptcha_iframe = test_driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')

solver.click_recaptcha_v2(iframe=recaptcha_iframe)

