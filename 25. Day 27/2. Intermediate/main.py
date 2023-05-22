from tkinter import *


# Button
def button_clicked():
    print("Button got clicked!")
    my_label.config(text="Button got clicked")
    new_text = user_input.get()
    my_label.config(text=new_text)


windows = Tk()
windows.title("My First GUI Program")
windows.minsize(width=500, height=300)
windows.config(padx=20, pady=20)

# Label
my_label = Label(text="I am not a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=100, y=100)
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click me!", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# 2nd Button
second_button = Button(text="Second button", command=button_clicked)
second_button.grid(column=2, row=0)

# Entry
user_input = Entry(width=10)
user_input.focus()
user_input.insert(END, "bro")
# user_input.pack()
user_input.grid(column=3, row=2)

windows.mainloop()
