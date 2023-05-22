from selenium import webdriver

AMAZON_FOOSBALL_TABLE_URL = "https://www.amazon.com/Hathaway-Foosball-56-Table-Cover/dp/B01LBBDUF8/ref=sr_1_35?crid" \
                            "=2GDFHNQTN22HQ&keywords=foosball&qid=1678870075&sprefix=foosbal%2Caps%2C507&sr=8-35"

chrome_web_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_web_path)

driver.get(url="https://www.python.org/")

# price = driver.find_element(by="class name", value="a-price-whole")
# print(price.text)
#
# search_bar = driver.find_element(by="name", value="q")
# print(search_bar.text)

# logo = driver.find_element(by="class name", value="python-logo")
# print(logo.size)

# logo = driver.find_element(by="css selector", value=".documentation-widget a")
# print(logo.text)

# logo = driver.find_element(by="xpath", value="//*[@id=\"site-map\"]/div[2]/div/ul/li[3]/a")
# print(logo.get_attribute(name="href"))

latest_news = driver.find_element(by="xpath", value="//*[@id=\"content\"]/div/section/div[2]/div[1]/div/ul")
latest_news = latest_news.text.split("\n")

latest_news_dict = {}
for x in range(0, len(latest_news) // 2, 2):
    latest_news_dict[x] = {"time": latest_news[x], "name": latest_news[x + 1]}
print(latest_news_dict)

driver.close()
driver.quit()
