from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
all_words = pandas.read_csv("data/french_words.csv")
french_words = all_words.French.to_list()
english_words = all_words.English.to_list()
random_french_word = ""
timer = ""
wrong_word_dict_passed = []

try:
    wrong_word_dict = pandas.read_csv("wrong_words_result.csv").to_dict()
    wrong_word_dict["French"] = [value for (key, value) in wrong_word_dict["French"].items()]
    wrong_word_dict["English"] = [value for (key, value) in wrong_word_dict["English"].items()]
    # del wrong_word_dict["Unnamed: 0"]
except FileNotFoundError or ValueError:
    wrong_word_dict = {"French": [], "English": []}

if wrong_word_dict["French"]:
    run_wrong_words = True
else:
    run_wrong_words = False


def trigger_wrong_button():
    global wrong_word_dict_passed
    global timer
    window.after_cancel(timer)
    if random_french_word not in wrong_word_dict["French"]:
        wrong_word_dict["French"].append(random_french_word)
        wrong_word_dict["English"].append(english_words[french_words.index(random_french_word)])
    if run_wrong_words and random_french_word not in wrong_word_dict_passed:
        wrong_word_dict_passed.append(random_french_word)
    pick_a_random_french_word()


def trigger_right_button():
    try:
        wrong_word_dict["English"].remove(english_words[french_words.index(random_french_word)])
        wrong_word_dict["French"].remove(random_french_word)
    except ValueError:
        pass
    pick_a_random_french_word()


def pick_a_random_french_word():
    global wrong_word_dict_passed
    global random_french_word, run_wrong_words

    not_found = True
    while run_wrong_words and not_found:
        if wrong_word_dict["French"] and len(wrong_word_dict["French"]) != len(wrong_word_dict_passed):
            random_french_word = random.choice(wrong_word_dict["French"])
            if random_french_word not in wrong_word_dict_passed:
                wrong_word_dict_passed.append(random_french_word)
                not_found = False
            else:
                not_found = True
        else:
            run_wrong_words = False
    if not run_wrong_words:
        random_french_word = random.choice(french_words)
    canvas.itemconfig(french_front_card, image=front_card)
    canvas.itemconfig(french_heading_card, text="French", fill="black")
    canvas.itemconfig(french_word_change, text=random_french_word, fill="black")
    timer_to_change_the_card()


def change_french_card_to_english_card():
    global random_french_word, run_wrong_words
    canvas.itemconfig(french_front_card, image=back_card)
    canvas.itemconfig(french_heading_card, text="English", fill="white")

    if run_wrong_words:
        canvas.itemconfig(french_word_change,
                          text=english_words[french_words.index(random_french_word)],
                          fill="white")
    else:
        canvas.itemconfig(french_word_change, text=english_words[french_words.index(random_french_word)], fill="white")


def timer_to_change_the_card():
    global timer
    timer = window.after(3000, change_french_card_to_english_card)


window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
french_front_card = canvas.create_image(400, 263, image=front_card)
french_heading_card = canvas.create_text(400, 150, text="French", font=(FONT_NAME, 40, "italic"))
french_word_change = canvas.create_text(400, 263, text=random_french_word, font=(FONT_NAME, 80, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
timer_to_change_the_card()

# Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=trigger_right_button)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=trigger_wrong_button)
wrong_button.grid(column=0, row=1)

pick_a_random_french_word()

# --- --- #
window.mainloop()
df = pandas.DataFrame(wrong_word_dict)
df.to_csv("wrong_words_result.csv", index=False)
