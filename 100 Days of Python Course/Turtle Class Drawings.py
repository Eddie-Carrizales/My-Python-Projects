# Author:      Eddie F. Carrizales
# Date:        07/01/2022
# Description: This program is simply a collection of mini drawing using the turtle class
# It draws a dashed line, draws shapes of different colors, draws a random walk, and draws a spirograph

import turtle
from turtle import *
import random

# Initialize screen
screen = Screen()
screen.setup(width=700, height=700)

#Draws a dashed line
def draw_dashed_line():

    # create new turtle object to draw
    new_turtle = Turtle()

    # Used to change/set the shape of our turtle object
    new_turtle.shape("classic")
    new_turtle.color("black")

    # go to first quadrant
    new_turtle.penup()
    new_turtle.setpos(-280,175)

    # Used to draw a dashed line
    for i in range(0, 10):
        new_turtle.pendown()
        new_turtle.forward(10)
        new_turtle.penup()
        new_turtle.forward(10)


# Draws shapes of different colors
def different_shapes_of_colors():
    # create new turtle object to draw
    new_turtle = Turtle()

    # Used to change/set the shape of our turtle object
    new_turtle.shape("turtle")
    new_turtle.color("green")

    # go to second quadrant
    new_turtle.penup()
    new_turtle.setpos(160,220)
    new_turtle.pendown()

    colors_list = ["orange", "blue", "green", "yellow", "red", "brown", "black", "purple"]

    shape_sides = 3

    while shape_sides < 10:
        current_side = 0
        shape_tilt = 360 / shape_sides
        while current_side != shape_sides:
            new_turtle.forward(40)
            new_turtle.right(shape_tilt)

            # generate random int and grab a random color from the color list
            rand_int = random.randint(0, len(colors_list)-1)
            rand_color = colors_list[rand_int]

            # change turtle and pen color
            new_turtle.pencolor(rand_color)
            new_turtle.color(rand_color)

            current_side += 1
        shape_sides += 1


# Draws a random walk
def random_walk():
    # create new turtle object to draw
    new_turtle = Turtle()

    # Used to change/set the shape of our turtle object
    new_turtle.shape("classic")
    new_turtle.color("black")

    # go to third quadrant
    new_turtle.penup()
    new_turtle.setpos(-175,-175)
    new_turtle.pendown()

    turtle.colormode(255) # required by turtle to use rgb

    # function to generate random values of r, g, b and return a random rgb tuple
    def random_color():
        # select random values for r, g, b
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        rgb_tuple = (r, g, b) # creates a rgb tuple

        return rgb_tuple

    # directions that will be randomly selected to move our turtle object
    direction_list = [0, 90, 180, 270]

    # Used to draw a dashed line
    new_turtle.speed(20)
    new_turtle.pensize(10)

    # loop to keep generating random colors and keep moving our object
    for i in range(0, 200):
        direction = direction_list[random.randint(0, 3)] # select a random direction

        # calls random_color function and to get and change pencolor to that color
        rand_color = random_color()
        new_turtle.pencolor(rand_color)

        # moves our new_turtle object in the random direction
        new_turtle.right(direction)
        new_turtle.forward(20)


# Draws a spirograph
def draw_spirograph():
    # create new turtle object to draw
    new_turtle = Turtle()

    # Used to change/set the shape of our turtle object
    new_turtle.shape("classic")
    new_turtle.color("black")
    new_turtle.speed(15)

    # go to first quadrant
    new_turtle.penup()
    new_turtle.setpos(175,-175)
    new_turtle.pendown()

    for i in range(40):
        new_turtle.circle(80)
        new_turtle.right(10)

def boundaries():
    # draws a vertical line
    vertical_line = Turtle()
    vertical_line.shape("square")
    vertical_line.shapesize(stretch_wid=36, stretch_len=0.5)

    # draws a horizontal line
    horizontal_line = Turtle()
    horizontal_line.shape("square")
    horizontal_line.shapesize(stretch_wid=0.5, stretch_len=36)

# run all the functions
boundaries()
draw_dashed_line()
different_shapes_of_colors()
random_walk()
draw_spirograph()

# create exit on screen click
# Note: this must be placed after everything else
screen.exitonclick()

