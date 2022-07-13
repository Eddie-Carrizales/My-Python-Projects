from turtle import Turtle
import random

# this class inherits everything from the Turtle class
class Food(Turtle):

    def __init__(self):
        super().__init__()
        # since we used the Turtle name next to Food and the super() above, this Food class
        # has now inherited everything from the Turtle class. This means that we can use the methods
        # that the Turtle class has such as the shape, penup, forward, color, etc. As seen below.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.new_random_food() # call to method

    def new_random_food(self):
        # Used to generate random x and y coordinates to give our food a random location
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)