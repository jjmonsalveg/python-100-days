from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self) -> None:
        return self.goto(STARTING_POSITION)
