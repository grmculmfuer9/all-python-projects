from turtle import *

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def counter_clockwise():
    tim.left(8)


def clockwise():
    tim.right(8)


def clear_the_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkeypress(key="Up", fun=forward)
screen.onkeypress(key="Left", fun=counter_clockwise)
screen.onkeypress(key="Right", fun=clockwise)
screen.onkeypress(key="Down", fun=backward)
screen.onkeypress(key="c", fun=clear_the_screen)

screen.exitonclick()
