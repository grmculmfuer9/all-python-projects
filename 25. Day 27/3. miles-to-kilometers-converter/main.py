from tkinter import *
import math

windows = Tk()
windows.title("Miles to Kilometer Convertor")
# windows.minsize(width=300, height=40)
windows.config(padx=40, pady=20)


def calculate_button_clicked():
    miles_number = float(miles_entry.get())
    final_result.config(text=math.ceil(miles_number * 1.609))


# Labels
text_label_equal_to = Label(text="is equal to", font=("Arial", 10, "bold"))
text_label_equal_to.grid(column=0, row=1)

# Result Label
final_result = Label(text=0, font=("Arial", 10, "bold"))
final_result.grid(column=1, row=1)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 10, "bold"))
miles_label.grid(column=2, row=0)

# Kms Label
kms_label = Label(text="Km", font=("Arial", 10, "bold"))
kms_label.grid(column=2, row=1)

# Entry for Miles
miles_entry = Entry(width=7)
miles_entry.focus()
miles_entry.insert(END, 0)
miles_entry.grid(column=1, row=0)

# Button to Calculate
calculate_button = Button(text="Calculate", command=calculate_button_clicked)
calculate_button.grid(column=1, row=2)

windows.mainloop()
