from turtle import Screen, Turtle, colormode
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "khaki3")
colormode(255)


def random_color(turtle: Turtle):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    turtle.pencolor(color)


def draw_shape():
    for _ in range(number_of_sides):
        angle = 360 / number_of_sides
        timmy.forward(100)
        timmy.right(angle)


number_of_sides = 3
while number_of_sides <= 10:
    random_color(timmy)
    draw_shape()
    number_of_sides += 1

my_screen = Screen()
my_screen.exitonclick()
