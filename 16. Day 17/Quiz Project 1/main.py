from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))

quiz = QuizBrain(question_bank)
while not quiz.still_has_question():
    value = quiz.next_question()

print("You've completed the quiz")
score = quiz.score
questions = quiz.question_number
print(f"Your final score was: {score}/{questions}")
