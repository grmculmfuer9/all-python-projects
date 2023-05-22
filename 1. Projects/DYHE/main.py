from tkinter import *

windows = Tk()
windows.title("Inter Student Industrial Services(ISIS)")
windows.config(padx=15, pady=18)

FONT_NAME = "Ariel"

canvas = Canvas(width=340, height=650)
canvas.create_text(250, 40, text="Home", font=(FONT_NAME, 8, "bold"))
canvas.grid(column=0, row=0)


windows.mainloop()
