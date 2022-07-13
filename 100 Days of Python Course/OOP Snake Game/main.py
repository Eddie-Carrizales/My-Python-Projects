# Author:      Eddie F. Carrizales
# Date:        07/04/2022
# Description: This is an OOP snake game controlled using the w, a, s, d keys.

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

# this will stop screen from refreshing/updating automatically
# thus to update the screen manually we can use scree.update()
screen.tracer(False)

# Create snake object
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun= snake.up)
screen.onkey(key="a", fun= snake.left)
screen.onkey(key="s", fun= snake.down)
screen.onkey(key="d", fun= snake.right)

game_is_on = True
while game_is_on:
    # update the screen every 0.1 seconds
    screen.update()
    time.sleep(0.1)

    # move snake forwards
    snake.move()

    # Detect if snake has collided with food
    if snake.snake_segments[0].distance(food) < 15:
        food.new_random_food()
        scoreboard.increase_scoreboard()
        snake.extend_snake()

    # Detect snake collision with wall
    if snake.snake_segments[0].xcor() > 280 or snake.snake_segments[0].xcor() < -280 or snake.snake_segments[0].ycor() > 280 or snake.snake_segments[0].ycor() < -280:
        game_is_on = False # the snake has hit a wall, thus game over
        scoreboard.game_over()

    # Detect collision with tail
    # We will use a python technique called slicing
    # example:
    # | a | b | c | d | e | f | g |
    # |   |   |   |   |   |   |   |
    # 0   1   2   3   4   5   6   7
    # thus if we use: letter_list[2:5] this will give us elements c, d, e since those are the once between the slices
    # We can also add an extra number at the end that will be the steps we want to take: letter_list[2:5:2]
    # If we want to get everything in the list but with different steps we can do: letter_list[::2] where 2 is 2 steps
    # using a neat trick we can do: letter_list[::-1], this will reverse the list as it will give all elements starting from the end

    #using slicing below, we can loop through every segment except for the first (snake_segment[0]), so we do from 1 to : everything
    for segment in snake.snake_segments[1:]:
        if snake.snake_segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()