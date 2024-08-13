import turtle as t
import random

# import colorgram

"""
colors = colorgram.extract("hirst_painting/image.jpg", 30)
rgb_colors = []

for color in colors:
    rgb_color = (color.rgb.r, color.rgb.g, color.rgb.b)
    rgb_colors.append(rgb_color)

print(rgb_colors)
"""

colors_list = [
    (249, 228, 17),
    (213, 13, 9),
    (198, 12, 35),
    (231, 228, 5),
    (197, 69, 20),
    (33, 90, 188),
    (43, 212, 71),
    (234, 148, 40),
    (33, 30, 152),
    (16, 22, 55),
    (66, 9, 49),
    (240, 245, 251),
    (244, 39, 149),
    (65, 202, 229),
    (14, 205, 222),
    (63, 21, 10),
    (224, 19, 111),
    (229, 165, 8),
    (15, 154, 22),
    (245, 58, 16),
    (98, 75, 9),
    (248, 11, 9),
    (222, 140, 203),
    (68, 240, 161),
    (10, 97, 62),
    (5, 38, 33),
    (68, 219, 155),
]

screen = t.Screen()
screen.setup(700, 700)

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")
tim.penup()
tim.hideturtle()
cordinate_x = -200
cordinate_y = -200
tim.goto((cordinate_x, cordinate_y))

for _ in range(10):
    tim.goto((cordinate_x, cordinate_y))
    for _ in range(10):
        tim.dot(20, random.choice(colors_list))
        tim.forward(50)
    cordinate_y += 50

screen.exitonclick()
