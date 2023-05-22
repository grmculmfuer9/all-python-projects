import os
import time
import random

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

INSTAGRAM_LOGIN_PAGE_URL = "https://www.instagram.com/"
INSTAGRAM_USERNAME = os.environ.get("instagram_username")
INSTAGRAM_EMAIL = os.environ.get("instagram_email")
INSTAGRAM_PASSWORD = os.environ.get("instagram_password")


def verify_follower_tab_open(follower_profile_link):
    topic_followers = ""
    try:
        topic_followers = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[3]/div/div/div["
                                                              "1]/div/div[2]/div/div/div/div/div[2]/div/div/div["
                                                              "1]/div/div[1]/h1/div").text.lower().strip()
    except NoSuchElementException:
        try:
            topic_followers = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div["
                                                                  "1]/div/div[2]/div/div/div/div/div["
                                                                  "2]/div/div/div[1]/div/div[1]/"
                                                                  "h1/div").text.lower().strip()
        except NoSuchElementException:
            if "followers" not in topic_followers:
                driver.get(url=f"{follower_profile_link}followers/")


def which_element_shows_followers():
    try:
        WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div["
                                                  "1]/div/div[2]/div/div/div/div/div["
                                                  "2]/div/div/div[2]/div[1]/div/div[1]")))
        return 0
    except TimeoutException:
        WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div["
                                                  "1]/div/div[2]/div/div/div/div/div["
                                                  "2]/div/div/div[2]/div[1]/div/div[1]")))
        return 1


def check_each_follower(current_profile_link):
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div["
                                                                          "2]/div/div/div[1]/div/div["
                                                                          "2]/div/div/div/div/div[2]/div/div/div["
                                                                          "2]/div[1]/div/div[1]")))
    time.sleep(2)

    count_followed = 0
    x = -1

    element_for_checking_followers = ["/html/body/div[2]/div/div/div[2]/div/div/div["
                                      f"1]/div/div[2]/div/div/div/div/div["
                                      f"2]/div/div/div[2]/div[1]/div/div[",
                                      "/html/body/div[2]/div/div/div[3]/div/div/div["
                                      f"1]/div/div[2]/div/div/div/div/div["
                                      f"2]/div/div/div[2]/div[1]/div/div["]
    final_element = element_for_checking_followers[which_element_shows_followers()]

    while count_followed < 30:
        print()
        x += 1
        time.sleep(3)
        verify_follower_tab_open(current_profile_link)
        WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, f"{final_element}{x + 1}]")))
        current_element = driver.find_element(By.XPATH, value=f"{final_element}{x + 1}]")
        driver.execute_script("arguments[0].scrollIntoView();", current_element)

        follow_status = current_element.find_element(By.CSS_SELECTOR, value="button div div").text.lower().strip()
        print(follow_status)

        if follow_status == "follow":
            a_href_tag = current_element.find_element(By.CSS_SELECTOR, value="div div div div div div "
                                                                             "div span div div div a")
            print(a_href_tag.get_attribute(name="href"))
            a_href_tag.click()

            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "body ._ac2a")))
            time.sleep(2)
            numbers_elements = driver.find_elements(By.CSS_SELECTOR, value="body ._ac2a")[1:]
            time.sleep(2)

            following = int("".join([i for i in numbers_elements[1].text.strip() if i.isnumeric()]))
            followers = int("".join([i for i in numbers_elements[0].text.strip() if i.isnumeric()]))
            print(followers, following)

            if following > 100 and (following / followers) > 1.9:
                count_followed += 1
                follow_button = driver.find_element(By.CSS_SELECTOR, value="body ._acan")
                follow_button.click()
                print(count_followed, 'count')
            driver.back()


def find_all_search_followers():
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "body .xieb3on li a")))
    details_profile = driver.find_elements(By.CSS_SELECTOR, value="body .xieb3on li a")

    for x in details_profile:
        x_href_link = x.get_attribute(name="href").lower().strip()
        if "followers" in x_href_link:
            x.click()
            return


def select_profile():
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/"
                                                  "div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div")))
    time.sleep(3)
    results_search_bar = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/"
                                                             "div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div")
    a_href_links_results_search_bar = results_search_bar.find_elements(By.CSS_SELECTOR, value="a")
    for x in a_href_links_results_search_bar:
        x_link = x.get_attribute(name="href").lower().strip()
        print(x_link)
        if "explore" not in x_link:
            x.click()
            return x_link


def input_search_bar():
    input_search_area = driver.find_element(By.CSS_SELECTOR, value="body ._aauy")
    input_search_area.send_keys(Keys.CONTROL + "a")
    input_search_area.send_keys("incomeparent")


def select_search_bar():
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, "body .x1iyjqo2")))
    time.sleep(3)
    side_bar = driver.find_element(By.CSS_SELECTOR, value="body .x1iyjqo2")
    WebDriverWait(side_bar, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "div div a"))
    )
    topics = [i.text.lower().strip() for i in
              side_bar.find_elements(By.CSS_SELECTOR, value="div div a div div div div") if i.text.strip() != ""]
    all_a_side_bar_links = side_bar.find_elements(By.CSS_SELECTOR, value="div div a")

    x = 0
    print(topics)
    for x in range(len(topics)):
        if topics[x] == "search":
            break
    print(x)
    all_a_side_bar_links[x].click()


chrome_web_path = "C:\\Development\\chromedriver.exe"
driver = Chrome(executable_path=chrome_web_path)

driver.maximize_window()
driver.get(url=INSTAGRAM_LOGIN_PAGE_URL)

try:
    WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.NAME, "username")))
    time.sleep(2)
    username_input = driver.find_element(By.NAME, value="username")
    username_input.send_keys(Keys.CONTROL + "a")
    username_input.send_keys(INSTAGRAM_USERNAME)

    password_input = driver.find_element(By.NAME, value="password")
    password_input.send_keys(Keys.CONTROL + "a")
    password_input.send_keys(INSTAGRAM_PASSWORD)

    sign_in_button = driver.find_element(By.CLASS_NAME, value="_acap")
    sign_in_button.click()
finally:
    try:
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, "_acap")))
        save_info_button = driver.find_element(By.CLASS_NAME, value="_acap")
        driver.execute_script("arguments[0].click();", save_info_button)
    finally:
        try:
            WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, "_a9_1")))
            not_now_button = driver.find_element(By.CLASS_NAME, value="_a9_1")
            driver.execute_script("arguments[0].click();", not_now_button)
        except TimeoutException:
            pass

while True:
    select_search_bar()
    input_search_bar()
    profile_link = select_profile()
    find_all_search_followers()
    check_each_follower(profile_link)
    time.sleep(random.randint(3700, 4000))
