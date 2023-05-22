from tkinter import *

windows = Tk()
windows.title("My First GUI Program")
windows.minsize(width=500, height=300)

# Label
my_label = Label(text="I am not a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    print("Button got clicked!")
    my_label.config(text="Button got clicked")
    new_text = user_input.get()
    my_label.config(text=new_text)


button = Button(text="Click me!", command=button_clicked)
button.pack()

# Entry
user_input = Entry(width=10)
user_input.pack()
user_input.focus()
user_input.insert(END, "bro")

# Text
text = Text(height=5, width=50)
text.focus()
text.insert(END, "Example of multi-line text entry")
print(text.get("1.0", END))
text.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    print(checkbutton_state.get())


checkbutton_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checkbutton_state, command=checkbutton_used)
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radio_button_1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radio_button_2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radio_button_1.pack()
radio_button_2.pack()


# ListBox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


windows.mainloop()
