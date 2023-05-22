import os
import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

SPEED_TEST_URL = "https://www.speedtest.net"
TWITTER_LOGIN_PAGE_URL = "https://twitter.com/i/flow/login"
TWITTER_USERNAME = os.environ.get("twitter_username")
TWITTER_EMAIL = os.environ.get("twitter_email")
TWITTER_PASSWORD = os.environ.get("twitter_password")
PROMISED_DOWNLOAD = 30
PROMISED_UP = 25

chrome_web_path = "C:\\Development\\chromedriver.exe"
driver = Chrome(executable_path=chrome_web_path)

driver.maximize_window()


def get_internet_speed():
    driver.get(url=SPEED_TEST_URL)

    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "body .hostUrl")))
    time.sleep(2)
    server = driver.find_element(By.CSS_SELECTOR, value="body .hostUrl")
    server = server.text.lower().strip()
    if "optimal" not in server or "finding" not in server or "server" not in server:
        time.sleep(2)
        try:
            go_button = driver.find_element(By.CSS_SELECTOR, value="body .test-mode-multi")
        except NoSuchElementException:
            go_button = driver.find_element(By.CSS_SELECTOR, value="body .js-start-test")
        driver.execute_script("arguments[0].scrollIntoView();", go_button)
        go_button.click()
        WebDriverWait(driver, 120).until(ec.presence_of_element_located((By.CSS_SELECTOR, "body .result-item-id")))
        WebDriverWait(driver, 120).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div["
                                                                               "3]/div/div/div/div[2]/div[3]/div["
                                                                               "3]/div/div[3]/div/div/div["
                                                                               "1]/div/div/div["
                                                                               "2]/div[2]/a")))
        result_id = driver.find_element(By.CSS_SELECTOR, value="body .result-item-id")
        driver.execute_script("arguments[0].scrollIntoView();", result_id)

        download_upload_result = driver.find_elements(By.CLASS_NAME, value="result-data-large")
        result_label = ["You download speed is ", "You upload speed is "]
        result_speed = []
        message_result = ""
        for x in range(len(download_upload_result)):
            result_speed.append(download_upload_result[x].text.lower().strip())
            message_result += result_label[x] + result_speed[x] + "\n"
        message_result = message_result.strip("\n")
        print(message_result)
        result_speed = [float(i) for i in result_speed]
        return result_speed


def tweet_to_provider(result_speed):
    message = f"Hey @StormFiberCare, why is my internet speed {result_speed[0]}down/{result_speed[1]}up," \
              f"when I pay for {PROMISED_DOWNLOAD}down/{PROMISED_UP}up."
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "body .public-DraftStyleDefault"
                                                                                     "-block")))
    time.sleep(3)
    tweet_textarea = driver.find_element(By.CSS_SELECTOR, value="body .public-DraftStyleDefault-block")
    tweet_textarea.click()
    tweet_textarea.send_keys(message)

    tweet_button = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div["
                                                       "1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div["
                                                       "3]/div/div/div[2]/div[3]")
    tweet_button.click()


def login_to_twitter():
    try:
        WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.NAME, "text")))
        time.sleep(2)
        username_input = driver.find_element(By.NAME, value="text")
        username_input.send_keys(Keys.CONTROL + "a")
        username_input.send_keys(TWITTER_USERNAME)

        time.sleep(2)
        username_input.send_keys(Keys.ENTER)

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, "password")))
        password_input = driver.find_element(By.NAME,
                                             value="password")
        password_input.send_keys(Keys.CONTROL + "a")
        password_input.send_keys(TWITTER_PASSWORD)

        login_button = driver.find_element(By.XPATH,
                                           value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div["
                                                 "2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
        login_button.click()
    except TimeoutException:
        print("Web page not loaded yet! Unstable Internet")
    except NoSuchElementException:
        print("Already Logged in")


speed_results = get_internet_speed()

driver.get(url=TWITTER_LOGIN_PAGE_URL)

login_to_twitter()

if PROMISED_DOWNLOAD > speed_results[0] or PROMISED_UP > speed_results[1]:
    tweet_to_provider(speed_results)

time.sleep(10)
