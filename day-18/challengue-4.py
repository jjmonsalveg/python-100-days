
import random
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
colours = ["red", "green","black","pink","red"]

timmy_the_turtle.color("red")

for sides in range(3,10):
    angle = 360 / sides
    timmy_the_turtle.color(random.choice(colours))
    for _ in range (sides):
        timmy_the_turtle.forward(50)
        timmy_the_turtle.right(angle)

screen = Screen()
screen.exitonclick()