import tkinter as tk
from tkinter import ttk

import requests
from bs4 import BeautifulSoup
from requests.exceptions import MissingSchema
from soupsieve.util import SelectorSyntaxError

is_request_loaded = False


def load_html():
    global soup, is_request_loaded
    try:
        response = requests.get(request_url_entry.get().lower().strip())
        is_request_loaded = True
    except MissingSchema:
        error.config(text="Please enter a valid URL")
        return
    error.config(text="")
    soup = BeautifulSoup(response.text, "html.parser")


def get_element_by_button():
    global soup, is_request_loaded
    print('hi')
    if not is_request_loaded:
        error.config(text="Please request a URL first")
        return
    error.config(text="")
    if dropdown_var.get() == "Class":
        print('hi')
        # print(get_element_by_class_name(get_element_by_entry.get()))
        condition, data = get_element_by_class_name(get_element_by_entry.get().strip())
        if condition:
            show_data(data)
    elif dropdown_var.get() == "ID":
        condition, data = get_element_by_id(get_element_by_entry.get().strip())
        if condition:
            show_data(data)
    elif dropdown_var.get() == "Other":
        condition, data = get_element_by_other(get_element_by_entry.get().strip())
        if condition:
            show_data(data)


def get_element_by_class_name(class_name):
    global is_request_loaded
    if not is_request_loaded:
        error.config(text="Please request a URL first")
        return None, None
    try:
        value = soup.select(f".{class_name}")
    except SelectorSyntaxError:
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
    try:
        value = soup.select(f"#{id_element}")
    except SelectorSyntaxError:
        error.config(text="Please enter a valid class name")
        return None, None
    error.config(text="")
    # print(value)
    return True, value


def get_element_by_other(other):
    global is_request_loaded
    if not is_request_loaded:
        error.config(text="Please request a URL first")
        return None, None
    try:
        value = soup.select(f"{other}")
    except SelectorSyntaxError:
        error.config(text="Please enter a valid class name")
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
soup = BeautifulSoup(parser="html.parser")

# Main Window
root = tk.Tk()
root.config(bg='#E6FFFD')
root.title("Custom Web Scraper")
root.geometry("900x650")
root.resizable(False, False)

# Title
# title = tk.Label(root, text="Custom Web Scraper", font=("Arial", 30), bg="#E6FFFD", fg="#B799FF")
# title.place(relx=0.5, rely=0.1, anchor="center")
title = ttk.Label(root, text="Custom Web Scraper", font=("Arial", 30), background="#E6FFFD", foreground="#B799FF")
title.place(relx=0.5, rely=0.1, anchor="center")

# Request URL
# request_url = tk.Label(root, text="URL", font=("Arial", 20), bg="#E6FFFD", fg="#B799FF")
# request_url.place(relx=0.25, rely=0.3, anchor="center")
request_url = ttk.Label(root, text="URL", font=("Arial", 20), background="#E6FFFD", foreground="#B799FF")
request_url.place(relx=0.25, rely=0.3, anchor="center")

# Request URL Entry
# request_url_entry = tk.Entry(root, font=("Arial", 20), bg="white", fg="#ACBCFF")
# request_url_entry.place(relx=0.5, rely=0.3, anchor="center")
request_url_entry = ttk.Entry(root, font=("Arial", 20), background="white", foreground="#ACBCFF")
request_url_entry.place(relx=0.5, rely=0.3, anchor="center")

# Request Button
request_button = tk.Button(root, text="Request", font=("Arial", 15), bg="#B799FF", fg="#E6FFFD", command=load_html,
                           activebackground="#B799FF", activeforeground="#E6FFFD", bd=0)
request_button.place(relx=0.75, rely=0.3, anchor="center")

# Get element by class name, id, other label
# get_element_by = tk.Label(root, text="Get Element By", font=("Arial", 20), bg="#E6FFFD", fg="#B799FF")
# get_element_by.place(relx=0.4, rely=0.5, anchor="center")
get_element_by = ttk.Label(root, text="Get Element By", font=("Arial", 20), background="#E6FFFD", foreground="#B799FF")
get_element_by.place(relx=0.4, rely=0.5, anchor="center")

# Get element by class name, id, other dropdown
# dropdown_var = tk.StringVar(root)
# dropdown_var.set("bro")
#
# # Create the OptionMenu with the arrow pointing downwards get_element_by_dropdown = tk.OptionMenu(root,
# dropdown_var, "Class Name", "ID", "Other", arrow="down") get_element_by_dropdown.config(font=("Arial", 20),
# width=3, bg="#B799FF", fg="#E6FFFD", activebackground="#B799FF", activeforeground="#E6FFFD")
# get_element_by_dropdown.place(relx=0.7, rely=0.5, anchor="center")

dropdown_var = tk.StringVar(root)

style = ttk.Style()
style.configure('Custom.TMenubutton', font=("Arial", 18), background="#B799FF", foreground="#E6FFFD")
style.map('Custom.TMenubutton',
          background=[('active', '#B799FF'), ('!active', '#B799FF')],
          foreground=[('active', '#E6FFFD'), ('!active', '#E6FFFD')])

get_element_by_dropdown = ttk.OptionMenu(root, dropdown_var, "Select", "Class", "ID", "Other",
                                         style='Custom.TMenubutton')
get_element_by_dropdown.place(relx=0.7, rely=0.5, anchor="center")

# Get element by class name, id, other entry
get_element_by_entry = ttk.Entry(root, font=("Arial", 20), background="white", foreground="#ACBCFF")
get_element_by_entry.place(relx=0.52, rely=0.6, anchor="center")

# Get element by class name, id, other button
get_element_by_button = tk.Button(root, text="Get Element", font=("Arial", 18), bg="#B799FF", fg="#E6FFFD",
                                  command=get_element_by_button, activebackground="#B799FF",
                                  activeforeground="#E6FFFD", bd=0)
get_element_by_button.place(relx=0.5, rely=0.7, anchor="center")

# Error Message
error = ttk.Label(root, text="", font=("Arial", 20), background="#E6FFFD", foreground="red")
error.place(relx=0.5, rely=0.9, anchor="center")

# Mainloop
root.mainloop()
