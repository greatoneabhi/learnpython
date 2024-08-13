from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(900, 500)

colors = ["red", "blue", "orange", "purple", "yellow", "green"]
y_axis = [-100, -50, 0, 50, 100, 150]
turtles = []

is_race_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-400, y_axis[turtle_index])
    turtles.append(new_turtle)

user_bet = screen.textinput(
    title="Make your bet.", prompt="Which turtle will win the race? Enter a color: "
)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 430:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
