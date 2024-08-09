# w = forwards
# s = backwards
# a = counter-clockwise
# d = clockwise
# c = clear drawing (return to initial pos)

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_fordwards():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    tim.left(10)
    
def move_right():
    tim.right(10)

def move_clear():
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(key="w", fun=move_fordwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=move_clear)

screen.exitonclick()


