# TODO. Create the Screen                (DONE)
# TODO. Create and move the paddle
# TODO. Create another paddle
# TODO. Create the ball and make it move (DONE)
# TODO. Collision with wall and bounce   (DONE)
# TODO. Detect collision with paddle
# TODO. Detect when paddle misses
# TODO. Keep score
from turtle import Screen

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
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

    # Detect ball collision with wall
    if ball.ycor() < -290 or ball.ycor() > 290:
        ball.bounce_y()

    # Detect ball collision with paddles
    if (
        ball.distance(r_paddle) <= 63.24
        and ball.xcor() >= 330
        or ball.distance(l_paddle) <= 63.24
        and ball.xcor() <= -330
    ):
        ball.bounce_x()

screen.exitonclick()
