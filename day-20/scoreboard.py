from turtle import Turtle

ALIGNMENT = "CENTER"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)
