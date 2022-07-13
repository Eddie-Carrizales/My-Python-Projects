from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.hideturtle()
        self.penup()
        self.setpos(-230, 270)
        self.write(f"Level: {self.counter}", move=False, align="center", font=FONT)

    def increase_scoreboard(self):
        """Clears the score board, adds 1 to the counter, and rewrites the scoreboard"""
        self.clear()
        self.counter += 1
        self.write(f"Level: {self.counter}", move=False, align="center", font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER.", move=False, align="center", font=FONT)
