
from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over.", align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 100
        self.clear()
        self.update_scoreboard()