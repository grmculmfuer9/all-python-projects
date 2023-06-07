import threading
import time
import tkinter as tk
from tkinter.messagebox import askyesno

from words import words

# Global Variables
words_english = words
stop = False
resume_testing = False
started = False
start_time = 0
incorrect_letters = 0


class KeyTracker:
    key = ''
    last_press_time = 0
    last_release_time = 0

    def track(self, key):
        self.key = key

    def is_pressed(self):
        return time.time() - self.last_press_time < .1

    def report_key_press(self, event):
        print(event.keysym, self.key)
        key_pressed()
        self.last_press_time = time.time()

    def report_key_release(self, event):
        if event.keysym == self.key:
            timer = threading.Timer(.1, self.report_key_release_callback, args=[event])
            timer.start()

    def report_key_release_callback(self, event):
        key_pressed()
        print(event.keysym)
        self.last_release_time = time.time()


def get_random_sentence():
    import random
    global words_english
    random_sentence_lst = random.sample(words_english, 10)
    random_sentence = ' '.join(random_sentence_lst) + ' '
    while len(random_sentence) < 280:
        random_sentence_lst = random.sample(words_english, 5)
        if len(' '.join(random_sentence_lst) + ' ') + len(random_sentence) <= 300:
            random_sentence += ' '.join(random_sentence_lst) + ' '
    return random_sentence.strip()


def start_button_function():
    global stop, resume_testing, start_time
    stop = False
    if resume_testing:
        key_pressed()
        resume_testing = False
    start_time = time.time()
    while True:

        if stop:
            stop = False
            show_time_label.config(text=f"Time: 0s")
            show_time_label.place(relx=0.57, rely=0.5, anchor="center")
            return

        time_diff = int(time.time() - start_time)
        show_time_label.config(text=f"Time: {time_diff}s")
        num = (58 - len(str(time_diff))) / 100
        show_time_label.place(relx=num, rely=0.5, anchor="center")
        root.update()


def reset_button_function():
    global stop, started
    stop = True
    started = False
    if askyesno("Reset", "Are you sure you want to reset?"):
        typing_test_entry.delete('1.0', tk.END)


def reset_button_complete():
    global stop, started
    stop = True
    started = False


def change_text():
    typing_test_text.config(state='normal')
    typing_test_text.delete('1.0', tk.END)
    typing_test_text.insert(tk.END, get_random_sentence())
    typing_test_text.config(state='disabled')


def key_pressed():
    global started, resume_testing, incorrect_letters
    print('ent')
    if not started:
        started = True
        resume_testing = True
        start_button.invoke()
    text_test = typing_test_entry.get('1.0', tk.END).strip('\n')
    text_start = typing_test_text.get('1.0', tk.END).strip('\n')
    for x in range(len(text_test)):
        # print('hm')
        if text_test[x] != text_start[x]:
            incorrect_letters += 1
            typing_test_entry.delete('1.0', tk.END)
            typing_test_entry.insert(tk.END, text_test[:x])
            break
    else:
        if len(text_test) == len(text_start):
            show_results()
            reset_button_complete()


def show_results():
    global start_time, incorrect_letters
    text_start = typing_test_text.get('1.0', tk.END)
    words_check = len(text_start.split())
    accuracy = 100 - round((incorrect_letters / 3) / len(text_start) * 100)
    wpm = round(words_check / (time.time() - start_time) * 60)
    print('wpm:', wpm, 'words:', words_check)
    results_text.config(state='normal')
    results_text.delete('1.0', tk.END)
    results_text.insert(tk.END, f"WPM: {wpm}\n\nAccuracy: {accuracy}%")
    results_text.config(state='disabled')


# Typing Master GUI

# Main Window
root = tk.Tk()
root.config(bg='#E6FFFD')
root.title("Typing Master")
root.geometry("900x650")
root.resizable(False, False)

# Title
title = tk.Label(root, text="Typing Master", font=("Arial", 30), bg="#E6FFFD", fg="#B799FF")
title.place(relx=0.5, rely=0.1, anchor="center")

# Typing test text
typing_test_text = tk.Text(root, font=("Arial", 15), bg="white", width=35, height=7, fg="#ACBCFF")
typing_test_text.place(relx=0.4, rely=0.35, anchor="center")
typing_test_text.insert(tk.END, get_random_sentence())
typing_test_text.config(state='disabled')

# Show time label
show_time_label = tk.Label(root, text="Time: 0s", font=("Arial", 15), bg="#E6FFFD", fg="#ACBCFF")
show_time_label.place(relx=0.57, rely=0.5, anchor="center")

# Typing test entry
key_tracker = KeyTracker()
typing_test_entry = tk.Text(root, font=("Arial", 15), bg="white", width=35, height=7, fg="#ACBCFF")
typing_test_entry.place(relx=0.4, rely=0.65, anchor="center")
typing_test_entry.focus()
typing_test_entry.bind_all("<KeyPress>", key_tracker.report_key_press)
typing_test_entry.bind_all('<KeyRelease>', key_tracker.report_key_release)

# Start button
start_button = tk.Button(root, text="Start", font=("Arial", 15), bg="white", width=7, height=1,
                         command=start_button_function, fg="#ACBCFF")
start_button.place(relx=0.3, rely=0.85, anchor="center")

# Reset button
reset_button = tk.Button(root, text="Reset", font=("Arial", 15), bg="white", width=7, height=1,
                         command=reset_button_function, fg="#ACBCFF")
reset_button.place(relx=0.5, rely=0.85, anchor="center")

# Change text button
change_text_button = tk.Button(root, text="Change Text", font=("Arial", 15), bg="white", width=12, height=1,
                               command=change_text, fg="#ACBCFF")
change_text_button.place(relx=0.4, rely=0.93, anchor="center")

# Results Text
results_text = tk.Text(root, font=("Arial", 15), bg="white", width=15, height=4, fg="#ACBCFF")
results_text.place(x=615, y=146)
results_text.insert(tk.END, "WPM: 0\n\nAccuracy: 0%")
results_text.config(state='disabled')

# Main Loop
root.mainloop()
