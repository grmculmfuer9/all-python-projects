import time

from selenium import webdriver
from selenium.webdriver.common.by import By

COOKIE_GAME_URL = "http://orteil.dashnet.org/experiments/cookie/"

chrome_web_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_web_path)

driver.get(url=COOKIE_GAME_URL)
store_items = driver.find_element(value="store")


def get_all_ids():
    ids_lst = []
    items_store = store_items.find_elements(By.CSS_SELECTOR, value="div")
    for x in items_store:
        ids_lst.append(x.get_attribute("id"))
    return ids_lst


def get_all_prices(available_money):
    elements_of_store_items = store_items.find_elements(By.CSS_SELECTOR, value="b")
    all_prices = []
    for x in elements_of_store_items:
        price = int(x.text.split("-")[1].strip())
        if price <= available_money:
            all_prices.append(price)
        else:
            break
    return all_prices


all_store_items_ids = get_all_ids()
while True:
    run_now = True
    count = time.time() + (60 * 5)

    while run_now:
        cookie = driver.find_element(value="cookie")
        cookie.click()
        if time.time() >= count:
            run_now = False
    money_available = int(driver.find_element(value="money").text)
    prices_of_all_items = get_all_prices(money_available)

    while prices_of_all_items != [] and prices_of_all_items[-1] <= money_available:
        money_available -= prices_of_all_items[-1]
        index_of_max_element = len(prices_of_all_items) - 1
        id_of_current_element = all_store_items_ids[index_of_max_element]
        item_to_be_clicked = driver.find_element(By.CSS_SELECTOR, value=f"#store #{id_of_current_element}")
        print(item_to_be_clicked.text)
        item_to_be_clicked.click()
        time.sleep(1)
        del prices_of_all_items[-1]
    time.sleep(5)
