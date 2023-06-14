from tkinter import ttk
import tkinter as tk

def dropdown_var_detect(*args):
    print('triggered dropdown_var_detect()')
    print(dropdown_var.get())


# Main Window
root = tk.Tk()
root.config(bg='#E6FFFD')
root.title("Custom Web Scraper")
root.geometry("900x650")
root.resizable(False, False)

# Title
title = ttk.Label(root, text="Custom Web Scraper", font=("Arial", 30), background="#E6FFFD", foreground="#B799FF")
title.place(relx=0.5, rely=0.1, anchor="center")

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
get_element_by_dropdown.bind('<<ComboboxSelected>>', dropdown_var_detect)

# Create a Combobox
combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox.bind("<<ComboboxSelected>>", dropdown_var_detect)
combobox.pack()

root.mainloop()
