import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong: Win at 7 points")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()

r_paddle.create_paddle()
l_paddle.create_paddle()

player1 = screen.textinput(title="Player 1 name", prompt="What is the name of player 1:")
player2 = screen.textinput(title="Player 2 name", prompt="What is the name of player 2:")

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.go_up)
screen.onkeypress(key="Down", fun=r_paddle.go_down)

screen.onkeypress(key="w", fun=l_paddle.go_up)
screen.onkeypress(key="s", fun=l_paddle.go_down)

game_is_on = True
ball.reset_position()
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_with_y()

    # Detect collision with r_paddle:
    if (ball.distance(r_paddle) < 55 and ball.xcor() > 350)\
            or (ball.distance(l_paddle) < 55 and ball.xcor() < -350):
        ball.bounce_with_x()

    # Detect if ball misses the right paddle
    if ball.xcor() > 370:
        ball.reset_position()
        ball.bounce_with_x()
        scoreboard.l_point()

    if ball.xcor() < -370:
        ball.reset_position()
        ball.bounce_with_x()
        scoreboard.r_point()

    if scoreboard.l_score == 7:
        scoreboard.write_the_winner(player1)
        game_is_on = False

    if scoreboard.r_score == 7:
        scoreboard.write_the_winner(player2)
        game_is_on = False

screen.exitonclick()
