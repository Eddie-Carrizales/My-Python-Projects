from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake() # call to method

    def create_snake(self):
        # loop creates starting segments of the snake with their characteristics
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def extend_snake(self):
        """This will add a segment at the position of the last snake segment ([-1] is used to access the last element of a list)"""
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        # range(start=2, stop=0, step= -1) unfortunately we cannot use keyword arguments on range
        for segment_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment_num - 1].xcor()
            new_y = self.snake_segments[segment_num - 1].ycor()
            self.snake_segments[segment_num].goto(new_x, new_y)

        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        # the snake is not allowed to go back on itself (otherwise it would touch its body)
        # thus we check if the head is heading the opposite direction, if it is not then
        # we allow it to change to the up direction, but if it is, we cannot allow it.
        # we do this for every movement: up, down, left, and right
        if self.snake_segments[0].heading() != DOWN:
            self.snake_segments[0].setheading(UP)

    def left(self):
        if self.snake_segments[0].heading() != RIGHT:
            self.snake_segments[0].setheading(LEFT)

    def down(self):
        if self.snake_segments[0].heading() != UP:
            self.snake_segments[0].setheading(DOWN)

    def right(self):
        if self.snake_segments[0].heading() != LEFT:
            self.snake_segments[0].setheading(RIGHT)