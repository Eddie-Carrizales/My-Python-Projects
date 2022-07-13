from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # keeps the ball moving
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    # allows the balls to bounce from the walls perpendicular to the y-axis (top and bottom walls)
    def bounce_y(self):
        self.y_move *= -1

    # allows the balls to bounce from the paddles
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # Used to reset the position of the wall, increase the speed and change the direction it will begin moving
    # this is called when the ball scores past any of the paddles
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
