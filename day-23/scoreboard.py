from turtle import Turtle

ALIGNMENT = "CENTER"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.goto(-240, 270)
        self.write(f"Level: {self.level}", True, align=ALIGNMENT, font=FONT)
