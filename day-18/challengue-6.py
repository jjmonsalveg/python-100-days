
import random
import turtle as t

tim = t.Turtle()
t.colormode(255)

direction = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

for _ in range(150):
    tim.color(random_color())
    tim.right(random.choice(direction))
    tim.forward(50)

screen = t.Screen()
screen.exitonclick()

