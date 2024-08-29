from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.speed("fast")
        self.setheading()
        
    def move(self):
        # x = self.xcor() + 1.3
        # y = self.ycor() + 1
        # self.goto(x,y)
        self.forward(2)