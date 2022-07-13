from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_scoreboard = 0
        self.right_scoreboard = 0
        self.update_scoreboard()

    # updates the scoreboard
    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.left_scoreboard, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.right_scoreboard, align="center", font=("Courier", 70, "normal"))

    # adds a point to the left paddle
    def left_point(self):
        self.clear()
        self.left_scoreboard += 1
        self.update_scoreboard()

    # add a point to the right paddle
    def right_point(self):
        self.clear()
        self.right_scoreboard += 1
        self.update_scoreboard()