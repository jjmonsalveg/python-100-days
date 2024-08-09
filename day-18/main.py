import random
import turtle as t

import colorgram

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()

_SPACE = 50
_DIAMETER = 20

colors = colorgram.extract("./day-18/colors.png", 25)
rgb_colors = []

for color in colors:
    rgb_colors.append(tuple(color.rgb))

tim.teleport(-200, -200)

for _ in range(10):
    y = tim.position()[1]

    for _ in range(10):
        tim.dot(_DIAMETER, random.choice(rgb_colors))
        x = tim.position()[0]
        tim.teleport(x + _SPACE, y)

    tim.teleport(-200, y + _SPACE)

screen = t.Screen()
screen.exitonclick()
