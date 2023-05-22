# Spirograph
from turtle import *
from random import randint


def draw_circle(x):
    color_random = random_turtle_color()
    tim.color(color_random)
    tim.circle(100)
    tim.right(x)


def random_turtle_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


colormode(255)
tim = Turtle()
tim.speed("fastest")

for i in range(int(360/5)):
    draw_circle(i)

screen = Screen()
screen.exitonclick()
