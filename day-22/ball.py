from turtle import Turtle

INITIAL_ANGLE = 36.87

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.speed("slowest")
        self.setheading(INITIAL_ANGLE)

    def move(self):
        self.forward(0.1)
