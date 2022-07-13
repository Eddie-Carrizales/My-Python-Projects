# Author:      Eddie F. Carrizales
# Date:        07/02/2022
# Description: This program will extract all the colors from a given image and use those colors to create a new similar painting.

import random
import turtle
from turtle import *
import colorgram

def extract_image_colors():
    """ function that will extract colors from an image using colorgram """

    rgb_colors = [] # initialize empty array
    colors = colorgram.extract('image.jpg', 100) # obtains up to 100 colors from given image name

    # loop to format the colors extracted as r, g, b and append those colors to our rgb_colors array/list
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)

    # will remove colors in our list that are white or shades of white since it is the background of our image
    rgb_colors.remove((250, 250, 249))
    rgb_colors.remove((246, 241, 244))

    return rgb_colors

def draw_painting():
    """function that will draw a painting using colors extracted from previous image"""

    color_list = extract_image_colors() # call to function to obtain color_list

    # Turtle initial set up
    turtle.colormode(255)
    new_turtle = Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(-275,-200)

    offset = -150 # off set used to reset the turtle at the end of every row
    num_of_dots = 101 # used as count

    # loop to keep turtle running and draw the dots
    for dot_count in range(1, num_of_dots):
        # moves the turtle forward and places a random color from our color list
        new_turtle.forward(50)
        new_turtle.dot(20, random.choice(color_list))

        # Conditional to reset the x position and move y position up by 50 at the end of each row
        if dot_count % 10 == 0:
            new_turtle.setposition(-275, offset)
            offset += 50

draw_painting() # call to function to start our program

# creates our screen and allows us to exit on click
screen = Screen()
screen.exitonclick()

