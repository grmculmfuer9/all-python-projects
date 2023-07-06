import os
import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

LINKEDIN_LOGIN_PAGE_URL = "https://www.linkedin.com/checkpoint/rm/sign-in-another-account?session_redirect=" \
                          "https%3A%2F%2Fwww.linkedin.com%2Ffeed%2F"
LINKEDIN_EMAIL = 'innocentdecentperson9@gmail.com'
LINKEDIN_PASSWORD = '03218050206_Ab'


def search_job(message):
    WebDriverWait(driver, 20).until(
        ec.presence_of_element_located((By.CLASS_NAME, "jobs-search-box__keyboard-text-input")))
    job_title = driver.find_element(By.CLASS_NAME, value="jobs-search-box__keyboard-text-input")
    job_title.send_keys(message)


def search_job_location(location):
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR,
                                        ".jobs-search-box__input--location .jobs-search-box__text-input")))
    job_location = driver.find_element(By.CSS_SELECTOR,
                                       value=".jobs-search-box__input--location .jobs-search-box__text-input")
    time.sleep(1)
    job_location.send_keys(location)

    id_job_location = job_location.get_attribute(name="id").split("-")[-1]
    count = 0
    for x in range(len(id_job_location) - 1, -1, -1):
        if not id_job_location[x].isnumeric():
            count = x
            break
    count += 1
    num = int(id_job_location[count:])
    ember = id_job_location[:count]
    if len(str(num)) == 2:
        num += 5
    else:
        num += 4
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, f"body #triggered-expanded-{ember}{num}")))
    time.sleep(2)
    print(ember, num)
    list_items = driver.find_element(By.CSS_SELECTOR, value=f"body #triggered-expanded-{ember}{num} li")
    time.sleep(2)
    list_items.click()


def easy_apply_filter():
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR,
                                        "body .search-reusables__all-filters-pill-button")))
    all_filter_button = driver.find_element(By.CSS_SELECTOR,
                                            value="body .search-reusables__all-filters-pill-button")
    all_filter_button.click()

    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[2]/ul")))
    ul_all_results = driver.find_element(By.XPATH, value="/html/body/div[3]/div/div/div[2]/ul")
    all_li_elements_ul = ul_all_results.find_elements(By.CSS_SELECTOR, value="li")
    easy_job_toggle_input = ""
    for x in range(2, len(all_li_elements_ul) + 1):
        text_h3_li_element = driver.find_element(by=By.XPATH,
                                                 value=f"/html/body/div[3]/div/div/div[2]/ul/li[{x}]/fieldset/h3").text
        if text_h3_li_element == "Easy Apply":
            easy_job_toggle_input = driver.find_element(by=By.XPATH,
                                                        value=f"/html/body/div[3]/div/div/div[2]/ul/li[{x}]/"
                                                              f"fieldset/div/"
                                                              "div/input")
            break

    driver.execute_script("arguments[0].scrollIntoView();", easy_job_toggle_input)
    driver.execute_script("arguments[0].click();", easy_job_toggle_input)

    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME,
                                        "search-reusables__secondary-filters-show-results-button")))
    show_the_results = driver.find_element(By.CLASS_NAME,
                                           value="search-reusables__secondary-filters-show-results-button")
    show_the_results.click()


def select_from_dropdown_options(x):
    options = x.find_element(By.CSS_SELECTOR, value="select")
    options.click()
    options_text = options.text.split("\n")[:-1]
    dropdown_options = [f"{i}. {options_text[i].strip()}" for i in range(len(options_text))]
    print(dropdown_options)
    select_dropdown_option = int(input("Which one do you want to select? Index starting from 0:\n"))
    option = options.find_elements(By.CSS_SELECTOR, value="option")[select_dropdown_option]
    driver.execute_script("arguments[0].scrollIntoView();", option)
    option.click()


def contact_info_fill_form():
    fields_on_current_page = driver.find_elements(By.CLASS_NAME, value="jobs-easy-apply-form-section__grouping")
    for x in fields_on_current_page:
        driver.execute_script("arguments[0].scrollIntoView();", x)
        label_of_field = x.find_element(By.CSS_SELECTOR, value="label").text.lower().strip()
        if "first" in label_of_field and "name" in label_of_field:
            input_box_field = x.find_element(By.CSS_SELECTOR, value="input")
            input_box_field.send_keys(Keys.CONTROL + "a")
            input_box_field.send_keys("Salman")
        elif "last" in label_of_field and "name" in label_of_field:
            input_box_field = x.find_element(By.CSS_SELECTOR, value="input")
            input_box_field.send_keys(Keys.CONTROL + "a")
            input_box_field.send_keys("Adnan")
        elif "email" in label_of_field:
            select_from_dropdown_options(x)
        elif "country" in label_of_field and "code" in label_of_field:
            select_from_dropdown_options(x)
        elif "phone" in label_of_field or "number" in label_of_field:
            input_box_field = x.find_element(By.CSS_SELECTOR, value="input")
            input_box_field.send_keys(Keys.CONTROL + "a")
            input_box_field.send_keys("3218050206")


def select_from_dropdown_checkbox_options(x):
    options = x.find_elements(By.CSS_SELECTOR, value="input")
    options_labels = x.find_elements(By.CSS_SELECTOR, value="label")
    lst_options_labels = []
    for y in range(len(options_labels)):
        lst_options_labels.append(f"{y}. {options_labels[y].text.strip()}")
    print(lst_options_labels)
    options_to_be_selected = input("Which options do you want to select? Give space in between them:\n")
    options_to_be_selected = [int(i) for i in options_to_be_selected.split()]
    for y in options_to_be_selected:
        driver.execute_script("arguments[0].scrollIntoView();", options[y])
        driver.execute_script("arguments[0].click();", options[y])


def select_from_dropdown_radio_options(x):
    options = x.find_elements(By.CSS_SELECTOR, value="input")
    options_labels = x.find_elements(By.CSS_SELECTOR, value="label")
    lst_options_labels = []
    for y in range(len(options_labels)):
        lst_options_labels.append(f"{y}. {options_labels[y].text.strip()}")
    print(lst_options_labels)
    option_to_be_selected = int(input("Which options do you want to select? Pick one:\n"))
    driver.execute_script("arguments[0].scrollIntoView();", options[option_to_be_selected])
    driver.execute_script("arguments[0].click();", options[option_to_be_selected])


def fill_input_box_field(x, message):
    input_box_field = x.find_element(By.CSS_SELECTOR, value="input")
    input_box_field.send_keys(Keys.CONTROL + "a")
    input_box_field.send_keys(message)


def additional_information_if_conditions(label, x):
    if "address" in label:
        fill_input_box_field(x, "Karachi")
    elif "city" in label:
        fill_input_box_field(x, "Karachi Division, Sindh, Pakistan")
    elif "state" in label:
        fill_input_box_field(x, "Karachi")
    elif "zip" in label:
        fill_input_box_field(x, "74800")
    elif "birth" in label and "date" in label:
        fill_input_box_field(x, "7/21/2004")
    elif "years" in label or "year" in label:
        fill_input_box_field(x, "1")
    elif "salary" in label:
        if "current" in label:
            fill_input_box_field(x, "100000")
        elif "expected" in label:
            fill_input_box_field(x, "120000")
        else:
            fill_input_box_field(x, "120000")
    elif "profile" in label:
        fill_input_box_field(x, "https://www.linkedin.com/in/hi-by-05636526a")
    else:
        try:
            WebDriverWait(x, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "input")))
            input_box_field = x.find_element(By.CSS_SELECTOR, value="input")
            is_checkbox = input_box_field.get_attribute(name="type").lower().strip()
            if is_checkbox == "checkbox":
                select_from_dropdown_checkbox_options(x)
            elif is_checkbox == "radio":
                select_from_dropdown_radio_options(x)
        except TimeoutException or NoSuchElementException:
            try:
                select_from_dropdown_options(x)
            except TimeoutException:
                fill_input_box_field(x, "I'm highly skilled AI/Data Scientist")


def additional_information():
    fields_on_current_page = driver.find_elements(By.CLASS_NAME, value="jobs-easy-apply-form-section__grouping")
    for x in fields_on_current_page:
        driver.execute_script("arguments[0].scrollIntoView();", x)
        label_of_field = x.find_element(By.CSS_SELECTOR, value="label").text.lower().strip()
        additional_information_if_conditions(label=label_of_field, x=x)


def easy_apply_to_specified_job():
    try:
        WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, ".jobs-apply-button--top-card button")))
        time.sleep(3)
        easy_apply_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-apply-button--top-card button")
        easy_apply_button.click()
        print(easy_apply_button.text, easy_apply_button.tag_name)
    except TimeoutException:
        return

    not_leave = True
    while not_leave:
        try:
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "body .pb4")))
            time.sleep(2)
            all_pb4_elements = driver.find_elements(By.CSS_SELECTOR, value="body .pb4")
            print([i.text for i in all_pb4_elements])
            print(0)
            print()
            for y in all_pb4_elements:
                driver.execute_script("arguments[0].scrollIntoView();", y)
                first_h3_field = y.find_element(By.CSS_SELECTOR, value="h3").text.lower().strip()
                print(first_h3_field)
                if "contact info" in first_h3_field:
                    contact_info_fill_form()
                elif "resume" in first_h3_field:
                    try:
                        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                                                                        "body .jobs-resume-picker"
                                                                                        "__resume-btn-container")))
                        resume_button = driver.find_element(By.CSS_SELECTOR,
                                                            value="body .jobs-resume-picker__resume-btn-container")
                        resume_button.click()
                    except TimeoutException:
                        pass
                else:
                    additional_information()
        except TimeoutException:
            pass

        try:
            WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH,
                                                                           "/html/body/div[3]/div/div/div[2]/div/"
                                                                           "div[2]/form/footer/div[2]/button")))
            next_buttons = driver.find_elements(By.XPATH,
                                                value="/html/body/div[3]/div/div/div[2]/div/div[2]/form/"
                                                      "footer/div[2]/button")
            for x in next_buttons:
                driver.execute_script("arguments[0].scrollIntoView();", x)
                h3_field_x = x.find_element(By.CSS_SELECTOR, value="span").text.lower().strip()
                print(h3_field_x)
                if h3_field_x == "next" or h3_field_x == "review":
                    x.click()
                elif h3_field_x == "submit application":
                    x.click()
                    not_leave = False
        except TimeoutException:
            try:
                WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH,
                                                                               "/html/body/div[3]/div/div/div["
                                                                               "2]/div/div[2]/div/footer/div["
                                                                               "2]/button["
                                                                               "2]")))
                submit_application_button = driver.find_element(By.XPATH,
                                                                value="/html/body/div[3]/div/div/div[2]/div/div["
                                                                      "2]/div/footer/div[2]/button[2]")
                driver.execute_script("arguments[0].scrollIntoView();", submit_application_button)
                submit_application_button.click()
                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located((By.CLASS_NAME, "artdeco-modal__dismiss")))
                time.sleep(3)
                close_feedback_message = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
                close_feedback_message.click()
                not_leave = False
            except TimeoutException:
                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                "/html/body/div[3]/div/div/div["
                                                                                "2]/div/div/form/footer/div["
                                                                                "3]/button")))
                submit_application_button = driver.find_element(By.XPATH,
                                                                value="/html/body/div[3]/div/div/div["
                                                                      "2]/div/div/form/footer/div[3]/button")
                driver.execute_script("arguments[0].scrollIntoView();", submit_application_button)
                submit_application_button.click()
                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located((By.CLASS_NAME, "artdeco-modal__dismiss")))
                time.sleep(3)
                close_feedback_message = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
                close_feedback_message.click()
                not_leave = False


def re_assign_all_job():
    return driver.find_elements(By.CLASS_NAME, value="jobs-search-results__list-item")


def apply_to_all_jobs():
    WebDriverWait(driver, 20).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, "body .jobs-search-results__list-item")))
    time.sleep(2)
    all_jobs = driver.find_elements(By.CSS_SELECTOR, value="body .jobs-search-results__list-item")
    for x in range(len(all_jobs)):
        # time.sleep(60)
        print(0)
        time.sleep(3)
        all_jobs = re_assign_all_job()
        driver.execute_script("arguments[0].scrollIntoView();", all_jobs[x])
        link_to_job_page = all_jobs[x].find_element(By.CSS_SELECTOR, value="a")
        link_to_job_page.click()
        easy_apply_to_specified_job()


# chrome_web_path = "C:\\Development\\chromedriver.exe"
# driver = Chrome(executable_path=chrome_web_path)
# Set up the Chrome WebDriver service
webdriver_service = Service(ChromeDriverManager().install())

print('start')

# Create a Chrome WebDriver instance
driver = Chrome(service=webdriver_service)
driver.maximize_window()

print('next')

driver.get(url=LINKEDIN_LOGIN_PAGE_URL)

print("let's go")

# time.sleep(5)
username = driver.find_element(value="username")
username.send_keys(LINKEDIN_EMAIL)

password = driver.find_element(value="password")
password.send_keys(LINKEDIN_PASSWORD)

sign_in = driver.find_element(By.CLASS_NAME, value="from__button--floating")
sign_in.click()

WebDriverWait(driver, 50).until(
    ec.presence_of_element_located((By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')))
go_to_jobs_page = driver.find_element(By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')
href_link_jobs_page = go_to_jobs_page.get_attribute(name="href")
driver.get(url=href_link_jobs_page)

search_job("Python Developer")

search_job_location("Karachi")

easy_apply_filter()

apply_to_all_jobs()

time.sleep(10)
