from turtle import *
from random import randint


def draw_shapes(n):
    length = 100
    angle = 360 / n
    for j in range(i):
        tim.forward(length)
        tim.right(angle)


def random_turtle_color():
    colr = (randint(0, 255), randint(0, 255), randint(0, 255))
    hexadecimal = ""
    hex_l = []
    for i in range(3):
        hex_l.append(hex(colr[i]).replace("0x", ""))
    for i in range(3):
        temp = hex_l[i]
        if len(temp) == 1:
            temp = "0" + temp
        hexadecimal += temp
    hexadecimal = "#" + hexadecimal
    tim.color(hexadecimal)


tim = Turtle()
tim.shape("turtle")

# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# for i in range(15):
#     tim.forward(15)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

for i in range(3, 11):
    random_turtle_color()
    draw_shapes(i)

screen = Screen()
screen.exitonclick()
