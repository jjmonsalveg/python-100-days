from turtle import Turtle

MOVE_DISTANCE = 20
SNAKE_WIDTH = 20
SNAKE_INITIAL_SIZE = 3
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class Snake:
    def __init__(self) -> None:
        self.segments: list[Turtle] = []
        self._create_snake()

    def _create_snake(self) -> None:
        for i in range(SNAKE_INITIAL_SIZE):
            self.add_segment((0 - i * SNAKE_WIDTH, 0))

    def add_segment(self, position: tuple):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()

        self.segments.clear()
        self._create_snake()

    def extend(self):
        self.add_segment(self.segments[-1].position())

    @property
    def head(self) -> Turtle:
        return self.segments[0]

    def move(self) -> None:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            prev_segment_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(prev_segment_pos)

        self.head.forward(MOVE_DISTANCE)

    def right(self) -> None:
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def up(self) -> None:
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def left(self) -> None:
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def down(self) -> None:
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)
