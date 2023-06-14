import tkinter as tk
from tkinter import ttk

from selenium import webdriver
from selenium.common import TimeoutException, InvalidArgumentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

is_request_loaded = False


def on_enter_button(e):
    e.widget['background'] = '#ACBCFF'


def on_leave_button(e):
    e.widget['background'] = '#B799FF'


def dropdown_var_detect(*args):
    print('triggered dropdown_var_detect()')
    print(args)
    value = dropdown_var.get()
    if value == "Class":
        instructions.config(text="Instruction:\nEnter the class name of the element you want to find")
    elif value == "ID":
        instructions.config(text="Instruction:\nEnter the ID of the element you want to find")
    elif value == "Partial Link Text":
        instructions.config(text="Instruction:\nEnter the partial link text of the element you want to find")
    elif value == "Link Text":
        instructions.config(text="Instruction:\nEnter the link text of the element you want to find")
    elif value == "Name":
        instructions.config(text="Instruction:\nEnter the name of the element you want to find")
    elif value == "Tag Name":
        instructions.config(text="Instruction:\nEnter the tag name of the element you want to find")
    elif value == "XPath":
        instructions.config(text="Instruction:\nEnter the XPath of the element you want to find")


def load_html():
    global is_request_loaded
    try:
        url = request_url_entry.get().strip()
        driver.get(url)
        is_request_loaded = True
    except InvalidArgumentException:
        error.config(text="Please enter a valid URL")
        return

    try:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "html")))
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "body")))
    except TimeoutException:
        error.config(text="Network error")
        return

    error.config(text="")


def get_element_by_button():
    global is_request_loaded
    if not is_request_loaded:
        error.config(text="Please request a URL first")
        return
    error.config(text="")
    if dropdown_var.get() == "Class":
        condition, data = get_element_by_class_name(get_element_by_entry.get().strip())
        if condition:
            show_data(data)
    elif dropdown_var.get() == "ID":
        condition, data = get_element_by_id(get_element_by_entry.get().strip())
        if condition:
            show_data(data)
    elif dropdown_var.get() == "Partial Link Text":
        condition, data = get_element_by_partial_link_text(get_element_by_entry.get().strip())
        if condition:
            show_data(data)
    elif dropdown_var.get() == "Link Text":
        condition, data = get_element_by_link_text(get_element_by_entry.get().strip())
        if condition:
            show_data(data)
    elif dropdown_var.get() == "Tag Name":
        condition, data = get_element_by_tag_name(get_element_by_entry.get().strip())
        if condition:
            show_data(data)
    elif dropdown_var.get() == "XPath":
        condition, data = get_element_by_xpath(get_element_by_entry.get().strip())
        if condition:
            show_data(data)
    elif dropdown_var.get() == "Name":
        condition, data = get_element_by_name(get_element_by_entry.get().strip())
        if condition:
            show_data(data)


def get_element_by_class_name(class_name):
    global is_request_loaded
    if not is_request_loaded:
        error.config(text="Please request a URL first")
        return None, None
    # try:
    #     value = soup.select(f".{class_name}")
    # except SelectorSyntaxError:
    try:
        print(class_name)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, class_name)))
        value = driver.find_elements(By.CLASS_NAME, class_name)
    except TimeoutException:
        error.config(text="Please enter a valid class name")
        return None, None
    error.config(text="")
    # print(value)
    return True, value


def get_element_by_id(id_element):
    global is_request_loaded
    if not is_request_loaded:
        error.config(text="Please request a URL first")
        return None, None
    # try:
    #     value = soup.select(f"#{id_element}")
    # except SelectorSyntaxError:
    try:
        print(id_element)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, id_element)))
        value = driver.find_elements(By.ID, id_element)
    except TimeoutException:
        error.config(text="Please enter a valid id")
        return None, None
    error.config(text="")
    # print(value)
    return True, value


def get_element_by_partial_link_text(partial_link_text):
    global is_request_loaded
    if not is_request_loaded:
        error.config(text="Please request a URL first")
        return None, None
    # try:
    #     value = soup.select(f"{partial_link_text}")
    # except SelectorSyntaxError:
    try:
        print(partial_link_text)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, partial_link_text)))
        value = driver.find_elements(By.PARTIAL_LINK_TEXT, partial_link_text)
    except TimeoutException:
        error.config(text="Please enter a valid partial link text")
        return None, None
    error.config(text="")
    # print(value)
    return True, value


def get_element_by_link_text(link_text):
    global is_request_loaded
    if not is_request_loaded:
        error.config(text="Please request a URL first")
        return None, None
    # try:
    #     value = soup.select(f"{link_text}")
    # except SelectorSyntaxError:
    try:
        print(link_text)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.LINK_TEXT, link_text)))
        value = driver.find_elements(By.LINK_TEXT, link_text)
    except TimeoutException:
        error.config(text="Please enter a valid link text")
        return None, None
    error.config(text="")
    # print(value)
    return True, value


def get_element_by_tag_name(tag_name):
    global is_request_loaded
    if not is_request_loaded:
        error.config(text="Please request a URL first")
        return None, None
    # try:
    #     value = soup.select(f"{tag_name}")
    # except SelectorSyntaxError:
    try:
        print(tag_name)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.TAG_NAME, tag_name)))
        value = driver.find_elements(By.TAG_NAME, tag_name)
    except TimeoutException:
        error.config(text="Please enter a valid tag name")
        return None, None
    error.config(text="")
    # print(value)
    return True, value


def get_element_by_xpath(xpath):
    global is_request_loaded
    if not is_request_loaded:
        error.config(text="Please request a URL first")
        return None, None
    # try:
    #     value = soup.select(f"{xpath}")
    # except SelectorSyntaxError:
    try:
        print(xpath)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath)))
        value = driver.find_elements(By.XPATH, xpath)
    except TimeoutException:
        error.config(text="Please enter a valid xpath")
        return None, None
    error.config(text="")
    # print(value)
    return True, value


def get_element_by_name(name):
    global is_request_loaded
    if not is_request_loaded:
        error.config(text="Please request a URL first")
        return None, None
    # try:
    #     value = soup.select(f"[name={name}]")
    # except SelectorSyntaxError:
    try:
        print(name)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, name)))
        value = driver.find_elements(By.NAME, name)
    except TimeoutException:
        error.config(text="Please enter a valid name")
        return None, None
    error.config(text="")
    # print(value)
    return True, value


def show_data(data_to_show):
    # create new tkinter window
    data_window = tk.Toplevel(root)
    data_window.config(bg='#E6FFFD')
    data_window.title("Data")
    data_window.geometry("900x650")
    data_window.resizable(False, False)

    # Title
    title_new_window = ttk.Label(data_window, text="Data", font=("Arial", 30), background="#E6FFFD",
                                 foreground="#B799FF")
    title_new_window.place(relx=0.5, rely=0.1, anchor="center")

    # Data
    data = tk.Text(data_window, font=("Arial", 15), bg="white", fg="#ACBCFF", width=60, height=20)
    data.place(relx=0.5, rely=0.55, anchor="center")

    final_data = ''
    print(len(data_to_show))
    for individual_data in data_to_show:
        print(str(individual_data))
        final_data += str(individual_data) + "\n"

    data.insert(tk.END, final_data)

    # Disable editing
    data.config(state=tk.DISABLED)

    # Add scrollbar to data yaxis
    scrollbar_y = ttk.Scrollbar(data_window, orient='vertical', command=data.yview)
    scrollbar_y.place(relx=0.875, rely=0.55, anchor="center", relheight=0.72)
    # scrollbar.pack(side="right", fill="y")

    # Configure data scrollbar
    data.config(yscrollcommand=scrollbar_y.set, wrap='none', height=20)

    # Add scrollbar to data xaxis
    scrollbar_x = ttk.Scrollbar(data_window, orient='horizontal', command=data.xview)
    scrollbar_x.place(relx=0.5, rely=0.916, anchor="center", relwidth=0.74)

    # Configure data scrollbar
    data.config(xscrollcommand=scrollbar_x.set, wrap='none')

    # Configure the scrollbar to adjust based on text height
    data.bind("<Configure>", lambda e: data.xview_moveto(1.0))


# Custom Web Scraper

# BeautifulSoup
options = Options()
# options.add_argument("--headless=chrome")
# options.add_argument("--disable-gpu")
# options.add_argument("--window-size=1920x1080")
# options.add_argument(
#     "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#     "Chrome/91.0.4472.124 Safari/537.36")
# options.add_argument("--enable-javascript")

chrome_web_path = "C:\\Development\\chromedriver.exe"

service = Service(chrome_web_path)

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

# Main Window
root = tk.Tk()
root.config(bg='#E6FFFD')
root.title("Custom Web Scraper")
root.geometry("900x650")
root.resizable(False, False)

# Title
title = ttk.Label(root, text="Custom Web Scraper", font=("Arial", 30), background="#E6FFFD", foreground="#B799FF")
title.place(relx=0.5, rely=0.1, anchor="center")

# Request URL
request_url = ttk.Label(root, text="URL", font=("Arial", 20), background="#E6FFFD", foreground="#B799FF")
request_url.place(relx=0.25, rely=0.3, anchor="center")

# Request URL Entry
request_url_entry = ttk.Entry(root, font=("Arial", 20), background="white", foreground="#ACBCFF")
request_url_entry.place(relx=0.5, rely=0.3, anchor="center")

# Request Button
request_button = tk.Button(root, text="Request", font=("Arial", 15), bg="#B799FF", fg="#E6FFFD", command=load_html,
                           activebackground="#B799FF", activeforeground="#AEE2FF", bd=0)
request_button.place(relx=0.75, rely=0.3, anchor="center")
request_button.bind("<Enter>", on_enter_button)
request_button.bind("<Leave>", on_leave_button)

# Get element by class name, id, other label
get_element_by = ttk.Label(root, text="Get Element By", font=("Arial", 20), background="#E6FFFD", foreground="#B799FF")
get_element_by.place(relx=0.4, rely=0.5, anchor="center")

# Get element by class name, id, other dropdown
dropdown_var = tk.StringVar(root)
dropdown_var.trace("w", dropdown_var_detect)

style = ttk.Style()
style.configure('Custom.TMenubutton', font=("Arial", 18), background="#B799FF", foreground="#E6FFFD")
style.map('Custom.TMenubutton',
          background=[('active', '#B799FF'), ('!active', '#B799FF')],
          foreground=[('active', '#E6FFFD'), ('!active', '#E6FFFD')])

get_element_by_dropdown = ttk.OptionMenu(root, dropdown_var, "Select", "Class", "ID", "Partial Link Text",
                                         "Link Text", "Name", "Tag Name", "XPath", style='Custom.TMenubutton')
get_element_by_dropdown.place(relx=0.7, rely=0.5, anchor="center")

# Get element by class name, id, other entry
get_element_by_entry = ttk.Entry(root, font=("Arial", 20), background="white", foreground="#ACBCFF")
get_element_by_entry.place(relx=0.52, rely=0.6, anchor="center")

# Get element by class name, id, other button
get_element_by_button = tk.Button(root, text="Get Elements", font=("Arial", 18), bg="#B799FF", fg="#E6FFFD",
                                  command=get_element_by_button, activebackground="#AEE2FF",
                                  activeforeground="#E6FFFD", bd=0)
get_element_by_button.place(relx=0.5, rely=0.7, anchor="center")
get_element_by_button.bind("<Enter>", on_enter_button)
get_element_by_button.bind("<Leave>", on_leave_button)

# Instructions
instructions = tk.Label(root, text="", font=("Arial", 14), bg="#E6FFFD", fg="blue")
instructions.place(relx=0.5, rely=0.8, anchor="center")

# Error Message
error = ttk.Label(root, text="", font=("Arial", 20), background="#E6FFFD", foreground="red")
error.place(relx=0.5, rely=0.9, anchor="center")

# Mainloop
root.mainloop()
