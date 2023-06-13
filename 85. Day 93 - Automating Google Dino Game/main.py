import time

import keyboard
from PIL import ImageGrab
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

OBSTACLE_AREA_COORDINATES = (380, 645, 950, 760)
GAME_AREA_COORDINATES = (20, 580, 800, 760)


def check_day():
    image = ImageGrab.grab(bbox=GAME_AREA_COORDINATES)
    lst_image = list(image.getdata())
    return lst_image.count((255, 255, 255)) > lst_image.count((83, 83, 83))


def check_obstacle():
    image = ImageGrab.grab(bbox=OBSTACLE_AREA_COORDINATES)
    lst_image = list(image.getdata())
    if check_day():
        return (83, 83, 83) in lst_image
    else:
        return (255, 255, 255) in lst_image


chrome_web_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_web_path)

# # Automating Chrome Dino Game on website https://elgoog.im/t-rex/
# driver.get("https://elgoog.im/t-rex/")
# Automating Chrome Dino Game on website chrome://dino/
try:
    driver.get("chrome://dino/")
except WebDriverException:
    pass
driver.maximize_window()

time.sleep(2)
# Pressing space to start the game
driver.find_element(value="t").send_keys(Keys.SPACE)
print('key sent')

# time.sleep(5)

while True:

    if check_obstacle():
        driver.find_element(value="t").send_keys(Keys.SPACE)
        print('obstacle')
        time.sleep(0.01)
        print('-------------------')

    if keyboard.is_pressed('q'):
        break
    else:
        pass
