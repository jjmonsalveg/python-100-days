import random
from turtle import Turtle

from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def move(self, increase_factor):
        self.goto(
            self.xcor() - STARTING_MOVE_DISTANCE - MOVE_INCREMENT * increase_factor,
            self.ycor(),
        )


class CarManager:
    def __init__(self) -> None:
        super().__init__()
        self.all_cars: Car = []
        self._increase_factor = 0

    def move(self):
        for index, car in enumerate(self.all_cars):
            car.move(self._increase_factor)

            if car.xcor() < -320:
                car.hideturtle()
                del self.all_cars[index]
                del car

    def add_car(self):
        position_tuple = (300, random.randint(-250, 250))
        new_car = Car(position_tuple)
        self.all_cars.append(new_car)

    def detect_collision(self, player: Player):
        for car in self.all_cars:
            if car.distance(player) < 20:
                return True

        return False

    def increase_speed(self):
        self._increase_factor += 0.1
