from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH ------------------------------- #
def search_the_file():
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
        result_data = data[website_entry.get().title()]
        messagebox.showinfo(title="Record Found", message=f"Email: {result_data['email']}\nPassword: "
                                                          f"{result_data['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File does not exist")
    except KeyError:
        messagebox.showinfo(title="Error", message="Record not found")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    data = {}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops!", message="Please make sure, you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation of your details",
                                       message=f"Your website is {website}\nYour email is {email}\nYour password "
                                               f"is {password}\nIs it okay to save them?")

        if is_ok:
            new_data = {
                website: {
                    "email": email,
                    "password": password
                }
            }

            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)

                    # Updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
            finally:
                with open(file="data.json", mode="w") as file:  # This way you can write the data
                    # Saving updated data
                    json.dump(data, file, indent=2)
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=53)
email_entry.insert(0, "ninjacombo99@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", highlightthickness=0, width=14, command=search_the_file)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
