from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.move_speed = STARTING_MOVE_DISTANCE

    def move(self):
        new_x = self.xcor() - self.move_speed
        self.goto(new_x, self.ycor())

    def reset_position(self):
        self.goto(300, random.randint(-250, 250))

    def level_up(self):
        self.move_speed += MOVE_INCREMENT
        self.move()
