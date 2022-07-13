from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.penup()
        self.goto(position)

    # moves paddle up
    def move_up(self):
        self.goto(self.xcor(), self.ycor()+20)

    # moves paddle down
    def move_down(self):
        self.goto(self.xcor(), self.ycor()-20)
