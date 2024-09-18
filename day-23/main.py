import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
scoreboard = Scoreboard()
car_manager = CarManager()
count = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    count += 1
    car_manager.move()

    if count % 6 == 0:
        car_manager.add_car()

    if car_manager.detect_collision(player):
        game_is_on = False
        scoreboard.game_over()
    
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.level_up()

screen.exitonclick()