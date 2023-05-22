from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WRONG_ANSWER_COLOR = "#FF0032"
TRUE_ANSWER_COLOR = "#03C988"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.color_change = self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Some question text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=wrong_image, highlightthickness=0, bg=THEME_COLOR, command=self.false_pressed)
        self.true_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        print(q_text)
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        answer = "True"
        self.check_the_answer(answer)

    def false_pressed(self):
        answer = "False"
        self.check_the_answer(answer)

    def check_the_answer(self, answer):
        is_answer_correct = self.quiz.check_answer(answer)
        # print(is_answer_correct)
        if is_answer_correct:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.give_feedback(True)
        else:
            self.give_feedback(False)

        if self.quiz.still_has_questions():
            new_q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=new_q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz has ended")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg=TRUE_ANSWER_COLOR)
        else:
            self.canvas.configure(bg=WRONG_ANSWER_COLOR)
        self.window.after(1000, self.change_back_to_normal)

    def change_back_to_normal(self):
        self.canvas.configure(bg="white")
