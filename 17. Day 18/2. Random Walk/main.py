# Generate Random Walk using Turtle Graphics
import turtle
from turtle import *
from random import randint, choice
# todo: thickness
# todo: random color
# todo: speed up

colormode(255)


def random_turtle_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


def walk(walk_direction):
    turtle_color = random_turtle_color()
    tim.color(turtle_color)
    tim.right(walk_direction)
    tim.forward(20)


tim = Turtle()
tim.width(5)
tim.speed("fastest")
directions = [0, 90, 180, 270]

for i in range(100):
    decided_direction = choice(directions)
    walk(decided_direction)

screen = Screen()
screen.exitonclick()
