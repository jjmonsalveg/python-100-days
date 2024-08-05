
import random
from turtle import Turtle, Screen

turtle = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

direction = [0, 90, 180, 270]
turtle.pensize(15)
turtle.speed("fastest")

for _ in range(150):
    turtle.color(random.choice(colours))
    turtle.right(random.choice(direction))
    turtle.forward(50)

screen = Screen()
screen.exitonclick()

