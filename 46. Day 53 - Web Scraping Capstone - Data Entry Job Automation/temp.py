from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

print('Enter the gmailid and password')
gmailId, passWord = map(str, input().split())
try:
    chrome_web_path = "C:\\Development\\chromedriver.exe"
    driver = Chrome(executable_path=chrome_web_path)
    driver.maximize_window()
    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' + \
               'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
               '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
    driver.implicitly_wait(15)

    loginBox = driver.find_element(By.XPATH, '//*[@id ="identifierId"]')
    loginBox.send_keys(gmailId)

    nextButton = driver.find_elements(By.XPATH, '//*[@id ="identifierNext"]')
    nextButton[0].click()

    passWordBox = driver.find_element(By.XPATH,
                                      '//*[@id ="password"]/div[1]/div / div[1]/input')
    passWordBox.send_keys(passWord)

    nextButton = driver.find_elements(By.XPATH, '//*[@id ="passwordNext"]')
    nextButton[0].click()

    print('Login Successful...!!')
except:
    print('Login Failed')
