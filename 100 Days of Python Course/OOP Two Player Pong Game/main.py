# Author:      Eddie F. Carrizales
# Date:        07/06/2022
# Description: This is an OOP two player Pong Game.
# The left paddle is controlled using the w and s keys.
# The right paddle is controlled using the up and down arrow keys.

from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

# Initialize screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(False)

# create game objects
scoreboard = Scoreboard()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

# allow input from the keyboard to control the paddles
screen.listen()
screen.onkey(key="Up", fun= right_paddle.move_up)
screen.onkey(key="Down", fun= right_paddle.move_down)
screen.onkey(key="w", fun= left_paddle.move_up)
screen.onkey(key="s", fun= left_paddle.move_down)

is_game_on = True

while is_game_on:
    # controls how long the ball sleeps before moving (thus the speed of the ball)
    time.sleep(ball.move_speed)
    screen.update()

    # keeps the ball moving
    ball.move()

    # Detect collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with a paddle
    if (ball.distance(left_paddle) < 50 and ball.xcor() < -330) or ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()

    # Determine if the right paddle was missed
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.left_point()

    # Determine if the left paddle was missed
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()