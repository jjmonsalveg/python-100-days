from turtle import Turtle


class Border:
    def __init__(self, width_screen, height_screen) -> None:
        self._square = Turtle()
        self._square.color("white")
        self._square.penup()
        self._square.goto(-width_screen / 2, height_screen / 2)
        self._square.pendown()
        self._square.pensize(3)

        for _ in range(2):
            self._square.forward(width_screen)
            self._square.right(90)
            self._square.forward(height_screen)
            self._square.right(90)

            self._square.hideturtle()
