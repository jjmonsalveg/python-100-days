# TODO. Create the Screen                (DONE)
# TODO. Create and move the paddle       (DONE)
# TODO. Create another paddle            (DONE)
# TODO. Create the ball and make it move (DONE)
# TODO. Collision with wall and bounce   (DONE)
# TODO. Detect collision with paddle     (DONE)
# TODO. Detect when paddle misses        (DONE)
# TODO. Keep score
from turtle import Screen

from ball import Ball
from paddle import Paddle
from border import Border
from scoreboard import Scoreboard
import time

WIDTH_SCREEN = 800
HEIGTH_SCREEN = 600

screen = Screen()
screen.setup(width=WIDTH_SCREEN, height=HEIGTH_SCREEN)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

Border(WIDTH_SCREEN, HEIGTH_SCREEN)
scoreboard = Scoreboard()

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
    time.sleep(0.005)
    screen.update()
    ball.move()

    # Detect ball collision with wall
    if ball.ycor() < -290 or ball.ycor() > 290:
        ball.bounce_y()

    # Detect ball collision with paddles
    if (
        ball.distance(r_paddle) <= 63
        and ball.xcor() == 330
        or ball.distance(l_paddle) <= 63
        and ball.xcor() == -330
    ):
        ball.bounce_x()
        
    # Detect when R paddle is miss
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()

    # Detect when L paddle is miss
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()

screen.exitonclick()
