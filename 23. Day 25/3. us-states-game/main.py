import turtle
from input import Input
from read_50_states import ReadAllStates
from place_the_coordinates import PlaceTheCoordinates

FONT = ("Arial", 20, "normal")

# Set up the screen
screen = turtle.Screen()
screen.setup(width=750, height=500)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Declare turtles, some objects from classes, and necessary variables
result_turtle = turtle.Turtle()
user_input = Input()
read_every_states = ReadAllStates()
print_coordinates = PlaceTheCoordinates()
score = 0
guessed_states = []
answer_state = ""

while score <= 50:
    answer_state = user_input.popup(score)

    if score == 50:
        score += 1
        continue

    if answer_state == "Exit":
        read_every_states.store_missing_states(guessed_states)
        break

    result = read_every_states.confirm_the_answer(answer_state)
    if result:
        score += 1
        print_coordinates.place_the_answer(result, answer_state)
        guessed_states.append(answer_state)

result_turtle.hideturtle()
result_turtle.penup()
if score > 30:
    result_turtle.write(arg="You Won!", align="center", font=FONT)
elif answer_state != "Exit":
    result_turtle.write(arg="You lost!", align="center", font=FONT)

turtle.mainloop()
