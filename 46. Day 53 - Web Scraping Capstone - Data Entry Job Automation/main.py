import os
import time

import lxml
import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
# from webdriver_manager.chrome import ChromeDriverManager
# from undetected_chromedriver import Chrome
# from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from undetected_chromedriver import Chrome

GOOGLE_FORMS_URL = "https://forms.gle/8FKBFfpES5unmBxEA"
GOOGLE_FORMS_RESPONSES_URL = "https://docs.google.com/forms/d/1FhZNUSb0xuJEwXs7pcGw_hg8JoUXmH5gjCvflbrA3zA/edit"
# GMAIL_LOGIN_LINK = "https://accounts.google.com/v3/signin/identifier?dsh=S956385975%3A1679503148942555&continue
# =https" \ "%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&ifkv" \
# "=AWnogHdV19hR_egdg8-sGT9-yg9o7lwsz87PJImVRQCLynsGOOO48bBMcC5d5B07ot25Av6GrJJnaQ&passive=1209600" \
# "&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
ZILLIOW_URL = 'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"mapBounds"%3A%7B' \
              '"west"%3A-122.729959859375%2C"east"%3A-122.136698140625%2C"south"%3A37.64410412680145%2C"north"%3A37' \
              '.90624640683134%7D%2C"mapZoom"%3A11%2C"isMapVisible"%3Afalse%2C"filterState"%3A%7B"price"%3A%7B"max' \
              '"%3A872627%7D%2C"beds"%3A%7B"min"%3A1%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"mp"%3A%7B"max"%3A3000%7D' \
              '%2C"auc"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"fsbo' \
              '"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"fsba"%3A%7B"value"%3Afalse%7D%7D%2C' \
              '"isListVisible"%3Atrue%7D'
GMAIL_EMAIL = os.environ.get("gmail_email")
GMAIL_PASSWORD = os.environ.get("gmail_password")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 "
                  "Safari/537.36 OPR/96.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}


def input_details_rent_housing(element, lst, count):
    element.click()
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(lst[count])


zillow_data = requests.get(url=ZILLIOW_URL, headers=header).text
soup = BeautifulSoup(markup=zillow_data, parser=lxml, features="lxml")

all_addresses = [i.text.strip() for i in soup.select(selector=".gdfTyO address")]
print(all_addresses)

prices = soup.find_all(name="div", class_="bqsBln")
all_prices_lst = []
for x in prices:
    temp = x.find(name="span").text.lower().strip().replace(",", "")
    temp_num = ""
    for y in temp[1:]:
        if y.isnumeric():
            temp_num += y
        else:
            break
    temp = int(temp_num)
    all_prices_lst.append(temp)
print(all_prices_lst)

all_links = soup.find_all(name="a", class_="gdfTyO")
all_links_lst = []
for x in all_links:
    temp_link = f'https://www.zillow.com/b/{x["href"].split("/")[-2]}/'
    all_links_lst.append(temp_link)
print(all_links_lst)

chrome_web_path = "C:\\Development\\chromedriver.exe"
driver = Chrome(executable_path=chrome_web_path)
driver.maximize_window()

driver.get(url=GOOGLE_FORMS_URL)

for x in range(len(all_addresses)):
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "body .whsOnd")))
    time.sleep(2)
    all_input_fields = driver.find_elements(By.CSS_SELECTOR, value="body .whsOnd")
    input_details_rent_housing(element=all_input_fields[0], lst=all_addresses, count=x)
    input_details_rent_housing(element=all_input_fields[1], lst=all_prices_lst, count=x)
    input_details_rent_housing(element=all_input_fields[2], lst=all_links_lst, count=x)

    submit_button = driver.find_element(By.CSS_SELECTOR, value="body .Y5sE8d")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    submit_button.click()

    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Submit another response")))
    submit_another_response_link = driver.find_element(By.PARTIAL_LINK_TEXT, value="Submit another response")
    submit_another_response_link.click()
    break

# driver.get(url=GMAIL_LOGIN_LINK)
#
# WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, "identifierId")))
# email_element = driver.find_element(value="identifierId")
# email_element.send_keys(Keys.CONTROL + "a")
# email_element.send_keys(GMAIL_EMAIL)
# email_element.send_keys(Keys.ENTER)
#
# # time.sleep(10000)
#
# WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "body .whsOnd")))
# time.sleep(6)
# password_element = driver.find_element(By.CSS_SELECTOR, value="body .whsOnd")
# password_element.send_keys(Keys.CONTROL + "a")
# password_element.send_keys(GMAIL_PASSWORD)
# password_element.send_keys(Keys.ENTER)
#
# WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "body .docs-homescreen-grid-item")))
# form_open = driver.find_element(By.CSS_SELECTOR, value="body .docs-homescreen-grid-item")
# form_open.click()

time.sleep(3)

driver.get(url=GOOGLE_FORMS_RESPONSES_URL)

WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "body .ThdJC")))
response_tab = driver.find_elements(By.CSS_SELECTOR, value="body .ThdJC")[1]
response_tab.click()

try:
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "body .iph-button"))
    )
    style_button = driver.find_element(By.CSS_SELECTOR, value="body .iph-button")
    style_button.click()
except TimeoutException:
    pass

WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div[1]/div[1]/div["
                                          "2]/div[1]/div[1]/div"))
)
link_to_sheets_button = driver.find_element(By.XPATH, value="/html/body/div[4]/div[2]/div[2]/div/div[1]/div[1]/div["
                                                            "2]/div[1]/div[1]/div")
time.sleep(3)
link_to_sheets_button.click()
link_to_sheets_button.click()

time.sleep(10000)
