# This code will not work in repl.it as there is no access to the colorgram package here.###
# We talk about this in the video tutorials##
"""
todo: 10 by 10
todo: 20 in size and space of 50
"""
from turtle import *
from random import choice
color_list = [(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Bring the pen such that the pattern feels in the middle
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

colormode(255)


def random_color():
    color_random = choice(color_list)
    return color_random


def color_dot_line():
    dot_color = random_color()
    tim.dot(20, dot_color)
    tim.forward(50)


def next_line():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(180)


for i in range(100):
    color_dot_line()
    if (i + 1) % 10 == 0:
        next_line()

screen = Screen()
screen.exitonclick()
