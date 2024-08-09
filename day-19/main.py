# w = forwards
# s = backwards
# a = counter-clockwise
# d = clockwise
# c = clear drawing (return to initial pos)

import random
from turtle import Screen, Turtle


def create_turtle(color: str, x: int, y: int) -> Turtle:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)

    return new_turtle


is_race_on = False
all_turtles: Turtle = []

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


for i in range(6):
    turtle = create_turtle(colors[i], -230, -100 + i * 50)
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

winning_color = None

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
