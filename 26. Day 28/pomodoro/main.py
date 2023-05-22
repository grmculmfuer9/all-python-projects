from tkinter import *
from tkinter import Tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Reset the timer immediately"""
    global timer
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="TIMER", fg=GREEN)
    checkmark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    """Start the timer accordingly, work, break, or long break"""
    global reps
    reps += 1

    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="BREAK", fg=RED)
        count_down(long_break_sec)
        # print(reps, '8')
    elif reps % 2 == 0:
        title_label.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)
        # print('ent', reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    """Count down the given amount of time"""
    global mark
    count = int(count)
    canvas.itemconfig(timer_text, text=f"{str(count // 60).zfill(2)}:{str(count % 60).zfill(2)}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            mark += "✔"
            checkmark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=30, bg=YELLOW)

canvas = Canvas(width=200, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 160, image=tomato_img)
timer_text = canvas.create_text(103, 178, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer = canvas.itemconfig(timer_text, text="00:00")

start_timer_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_timer_button.config(highlightcolor="blue", bg=YELLOW)
start_timer_button.grid(column=0, row=2)

end_timer_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
end_timer_button.config(highlightcolor="blue", bg=YELLOW)
end_timer_button.grid(column=2, row=2)

title_label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 50, "bold"), highlightthickness=0, bg=YELLOW)
title_label.grid(column=1, row=0)

checkmark_label = Label(text="", fg=GREEN)
checkmark_label.config(bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()
