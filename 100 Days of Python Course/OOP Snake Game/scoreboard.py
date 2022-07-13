from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(0, 280)
        self.write(f"Score: {self.counter}", move=False, align="center", font=("Courier", 15, "normal"))

    def increase_scoreboard(self):
        """Clears the score board, adds 1 to the counter, and rewrites the scoreboard"""
        self.clear()
        self.counter +=1
        self.write(f"Score: {self.counter}", move=False, align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        self.setpos(0,0)
        self.write("GAME OVER.", move=False, align="center", font=("Courier", 20, "normal"))