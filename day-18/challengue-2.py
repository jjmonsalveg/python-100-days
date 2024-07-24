from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("arrow")
timmy_the_turtle.color("black")

for _ in range(15):
    timmy_the_turtle.forward(5)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(5)
    timmy_the_turtle.pendown()

screen = Screen()
screen.exitonclick()

