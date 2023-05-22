import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

LONDON_APP_BREWERY_URL = "https://londonappbrewery.com/sendy/subscription?f" \
                         "=m7Xj2bDOCQnlJ27yezLEAtJi1mhUIxOaJcJGZYMLLX6wx5MZd0b2FunBI8dOomNt&_ga=2.126018511.310966246" \
                         ".1678903997-608938908.1678903997"

chrome_web_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_web_path)

driver.get(url=LONDON_APP_BREWERY_URL)

user_name = driver.find_element(by="id", value="name")
user_name.send_keys("Salman Adnan")

user_email = driver.find_element(by="id", value="email")
user_email.send_keys("hellomy98d@gmail.com")

container = driver.find_element(By.CLASS_NAME, value="recaptcha-token")

click_button = driver.find_element(by="id", value="submit")
click_button.click()

time.sleep(5)
