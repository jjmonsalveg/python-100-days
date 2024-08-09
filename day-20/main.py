# TODO. 
# Create a snake  body
# move the snake
# create snake food
# detect collision with foo
# create a scoreboard
# detect collision with wall
# detect collision with tail

from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

def create_snake() -> list[Turtle]:
   snake: list[Turtle] =  []

   for i in range(3):
      segment = Turtle(shape="square")
      segment.color("white")
      segment.teleport(0 - i * 20 , 0)
      snake.append(segment)

   return snake


snake: list[Turtle] = create_snake()


screen.exitonclick()