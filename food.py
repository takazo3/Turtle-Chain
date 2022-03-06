import random
from turtle import Turtle
import random
COLOR = ["red", "blue", "Yellow", "white"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color(random.choice(COLOR))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.color(random.choice(COLOR))
        self.pu()
        self.goto(x, y)
