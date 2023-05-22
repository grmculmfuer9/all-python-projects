from turtle import Turtle
import time

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the snake in the beginning"""
        for position in START_POSITIONS:
            self.add_segment(position)

    def move(self):
        """Move the snake forward by 20 paces in the direction it is already moving"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Head the direction of the snake upwards if it is not facing downwards"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Head the direction of the downwards upwards if it is not facing upwards"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Head the direction of the snake leftwards if it is not facing rightwards"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Head the direction of the snake rightwards if it is not facing leftwards"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend_snake(self):
        """Extend the snake"""
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        """Add new segments to the snake"""
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        # new_segment.shapesize(stretch_wid=0.5, stretch_len=0.5)
        new_segment.goto(position)
        new_segment.speed("fastest")
        self.segments.append(new_segment)
