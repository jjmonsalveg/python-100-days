# TODO. Create the Screen                (DONE)
# TODO. Create and move the paddle
# TODO. Create another paddle
# TODO. Create the ball and make it move
# TODO. Collision with wall and bounce
# TODO. Detect collision with paddle
# TODO. Detect when paddle misses
# TODO. Keep score
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(( 350, 0 ))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

screen.exitonclick()
