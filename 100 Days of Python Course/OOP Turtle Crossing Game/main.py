# Author:      Eddie F. Carrizales
# Date:        07/07/2022
# Description: This is an OOP turtle crossing game.
# The turtle is controlled using the Up arrow key or the "w" key.

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

# create objects
crossing_turtle = Player()
scoreboard = Scoreboard()
cars = CarManager()

# listen to keystrokes
screen.listen()
screen.onkey(key="Up", fun= crossing_turtle.move_up)
screen.onkey(key="w", fun= crossing_turtle.move_up)

game_is_on = True
loop_counter = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # A car will generate every 6 loops
    if loop_counter % 6 == 0:
        cars.create_car()

    cars.move()

    for i in range(0, len(cars.car_list)):
        if crossing_turtle.distance(cars.car_list[i]) < 25:
            game_is_on = False
            scoreboard.game_over()

    # If player has reached the other side (reached the finish line)
    if crossing_turtle.ycor() > 280:
        crossing_turtle.reset_position()
        cars.increase_speed()
        scoreboard.increase_scoreboard()

    loop_counter +=1

screen.exitonclick()