from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.reset_velocity()

    def move(self):
        y = self.ycor() + self.delta_y
        x = self.xcor() + self.delta_x
        self.goto(x, y)

    def bounce_y(self):
        self.delta_y *= -1

    def bounce_x(self):
        self.increase_velocity()
        self.delta_x *= -1

    def increase_velocity(self):
        if self.delta_x < 0:
            self.delta_x -= 1
        else:
            self.delta_x += 1

        if self.delta_y < 0:
            self.delta_y -= 1
        else:
            self.delta_y += 1

    def reset_velocity(self):
        self.delta_y = 1
        self.delta_x = 1

    def reset(self):
        self.reset_velocity()
        self.goto(0, 0)
        self.bounce_x()
