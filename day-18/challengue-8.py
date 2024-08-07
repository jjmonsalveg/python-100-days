import random
import turtle as t

tim = t.Turtle()
t.colormode(255)

tim.speed("fastest")
tim.hideturtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        tim.circle(50)
        tim.color(random_color())
        print(tim.heading())
        print(f"suma:{tim.heading() + size_of_gap}")
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(1)
screen = t.Screen()
screen.exitonclick()
