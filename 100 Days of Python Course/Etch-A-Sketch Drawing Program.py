# Author:      Eddie F. Carrizales
# Date:        07/03/2022
# Description: This program is a simple etch-a-sketch game that is controlled by the a,w,s,d, to draw anything the user wants.

from turtle import Turtle, Screen

#initialize turtle and screen
new_turtle = Turtle()
screen = Screen()

# functions called by the controls to move and turn
def move_forwards():
    new_turtle.forward(10)

def move_backwards():
    new_turtle.backward(10)

def counter_clockwise():
    new_turtle.left(10)

def clockwise():
    new_turtle.right(10)

def clear_screen():
    # clears screen and returns turtle to center
    new_turtle.clear()
    new_turtle.penup()
    new_turtle.home()
    new_turtle.pendown()

# etch-a-sketch controls
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)

# exit screen on click
screen.exitonclick()