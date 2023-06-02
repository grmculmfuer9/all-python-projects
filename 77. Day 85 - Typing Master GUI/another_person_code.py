import os
import random
import tkinter as tk
from time import time
from tkinter import ttk

import requests
from playsound import playsound

HEADERS = {
    "X-Api-Key": 'MYAPIKEY'
}

punc_list = [".", ",", "!", "?"]
an = ["An", "A"]
vowels = ["a", "e", "i", "o", "u"]
word_types = ["adjective", "noun", "verb", "adverb"]
sentences = [
    ["A", "bad", "cat", "eats", "soothingly."],
    ["An", "ignorant", "dog", "sleeps", "loudly!"],
    ["A", "deafening", "girrafe", "goes", "quickly?"],
    ["A", "good-looking", "salesman", "irrigates", "amazingly,"],
    ["An", "interesting", "computer", "walks", "angrily!"]

]
# sentences = [["a"], ["a"], ["a"], ["a"], ["a"]]
api_url = 'https://api.api-ninjas.com/v1/randomword'
prev_time = 0
elapsed_time = []
failed_attempts = 0


def new_words():
    sentences.clear()
    pb["value"] = 0
    for i in range(5):
        sentences.append([""])
        for word_type in word_types:
            if word_type == "verb":
                sentences[i].append(requests.get(
                    api_url, params={"type": word_type},
                    headers=HEADERS).json()["word"] + "s"
                                    )
            else:
                sentences[i].append(requests.get(
                    api_url, params={"type": word_type},
                    headers=HEADERS).json()["word"]
                                    )
            pb["value"] += 5
            win.update()
        case = sentences[i][1][0] not in vowels
        sentences[i][0] = an[case]
        punc = random.choice(punc_list)
        sentences[i][-1] += punc
    update_word_box()


def update_word_box():
    global prev_time
    prev_time = 0
    elapsed_time.clear()
    text_entry.config(state="normal")
    text_entry.delete("0", tk.END)
    text_entry.insert(tk.END, "Press 'ENTER' to begin...")

    word_box.config(state="normal")
    word_box.delete("1.0", tk.END)
    for sentence in sentences:
        for word in sentence:
            word_box.insert(tk.END, word + " ")
        word_box.insert(tk.END, "\n")
    word_box.delete("6.0", tk.END)
    word_box.config(state="disabled")


def check_line():
    line = word_box.get("1.0", "2.0").replace("\n", "")[:-1]
    return text_entry.get() == line


def new_line(*args):
    win.update()
    global prev_time
    global failed_attempts
    word_box.config(state="normal")
    if prev_time != 0:
        if check_line():
            audio_file = os.path.dirname(__file__) + '\\success.mp3'
            playsound(audio_file)
            word_box.delete("1.0", "2.0")
        else:
            audio_file = os.path.dirname(__file__) + '\\buzzer.mp3'
            playsound(audio_file)
            failed_attempts += 1
        elapsed_time.append((time() - prev_time))
    text_entry.delete("0", tk.END)
    prev_time = time()
    if len(word_box.get("1.0", tk.END)) <= 1:
        game_end()
    word_box.config(state="disabled")


def game_end():
    characters = 0
    for sentence in sentences:
        for word in sentence:
            characters += len(word) + 1
    total_time = sum(elapsed_time)
    char_per_min = (characters / total_time) * 60
    word_per_min = char_per_min / 5
    word_box.config(state="normal")
    word_box.insert(tk.END, f"""Congratulations!
    You've typed {characters} charecters!
    It took you {round(total_time)} seconds!
    That's {round(char_per_min)} cpm,
    or {round(word_per_min)} wpm!""")
    word_box.config(state="disabled")
    text_entry.config(state="disabled")


win = tk.Tk()
win.config(bg="#be6c41")
word_box = tk.Text(win, width=60, height=5, state="disabled")
word_box.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
new_words_btn = tk.Button(win, text="New Text", command=new_words)
new_words_btn.grid(row=1, column=0, sticky="EW", padx=10)
pb = ttk.Progressbar(win, orient="horizontal", mode="determinate", length=200)
pb.grid(row=1, column=1, sticky="EW", padx=10)
text_entry = tk.Entry(win)
text_entry.grid(row=2, column=0, columnspan=2, sticky="EW", padx=10, pady=10)
text_entry.bind("<Return>", new_line)
text_entry.insert(tk.END, "Press 'ENTER' to begin...")
text_entry.focus()

update_word_box()

win.mainloop()
