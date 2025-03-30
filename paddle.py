from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=5)
        self.penup()
        self.goto(position)
        self.setheading(UP)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)