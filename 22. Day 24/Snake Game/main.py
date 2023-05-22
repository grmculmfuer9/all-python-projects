# Snake Game
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from walls import  Walls
import time

screen = Screen()
screen.setup(width=620, height=620)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
walls = Walls()

walls.make_wall()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increment()
        snake.extend_snake()

    # Extend the snake when it eats the food
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset_score()
        snake.reset()

    # Detect collision with the food
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset()

screen.exitonclick()
