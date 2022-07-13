from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.car_list = []
        self.create_car()
        self.speed = 0

    def create_car(self):
        new_car = Turtle(shape= "square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.penup()

        # generate a random color for each new car
        random_color = random.choice(COLORS)
        new_car.color(random_color)

        # generate a random y_position for each new car
        y_position = random.randint(-250, 250)
        new_car.goto(300, y_position)

        #add the car to our list
        self.car_list.append(new_car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def move(self):
        for i in range(0, len(self.car_list)):
            self.car_list[i].forward(STARTING_MOVE_DISTANCE + self.speed)
