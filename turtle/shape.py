from turtle import Turtle
from random import random


class Shape:

    def __init__(self, sides, angle):
        self.sides = sides
        self.angle = angle

    def draw(self, side_length, turtle: Turtle):
        random_color(turtle)
        for _ in range(self.sides):
            turtle.forward(side_length)
            turtle.right(self.angle)


def random_color(turtle: Turtle):
    r = random()
    g = random()
    b = random()
    color = (r, g, b)
    turtle.pencolor(color)
