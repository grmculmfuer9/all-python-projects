from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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

    password_list = []

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 and len(email) == 0 and len(password) == 0:
        messagebox.showwarning(title="Missing Details", message="Website, email and password not entered")
        break_the_function = True
    elif len(website) == 0 and len(password) == 0:
        messagebox.showwarning(title="Missing Details", message="Website and password not entered")
        break_the_function = True
    elif len(website) == 0 and len(email) == 0:
        messagebox.showwarning(title="Missing Details", message="Website and email not entered")
        break_the_function = True
    elif len(email) == 0 and len(password) == 0:
        messagebox.showwarning(title="Missing Details", message="Email and password not entered")
        break_the_function = True
    elif len(website) == 0:
        messagebox.showwarning(title="Missing Details", message="Website not entered")
        break_the_function = True
    elif len(password) == 0:
        messagebox.showwarning(title="Missing Details", message="Password not entered")
        break_the_function = True
    elif len(email) == 0:
        messagebox.showwarning(title="Missing Details", message="Email not entered")
        break_the_function = True

    if break_the_function:
        return

    is_ok = messagebox.askokcancel(title="Confirmation of your details",
                                   message=f"Your website is {website}\nYour email is {email}\nYour password "
                                           f"is {password}\nIs it okay to save them?")

    if is_ok:
        with open(file="data.txt", mode="a") as file:
            file.write(f"{website} | {email} | {password}\n")
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
website_entry = Entry(width=53)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=3)

email_entry = Entry(width=53)
email_entry.insert(0, "ninjacombo99@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
