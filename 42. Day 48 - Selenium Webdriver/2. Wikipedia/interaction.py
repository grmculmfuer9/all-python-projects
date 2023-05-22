from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_web_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_web_path)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

articles_number = driver.find_element(by="css selector", value="#articlecount a")
# articles_number.click()

# all_portals = driver.find_element(by="link text", value="All portals")
# all_portals.click()

search = driver.find_element(by="name", value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

time.sleep(5)

# driver.quit()
