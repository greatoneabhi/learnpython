from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_right.color("blue")
paddle_left = Paddle((-350, 0))
paddle_left.color("Green")
ball = Ball()
ball.color("yellow")
Scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")

screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

game_is_one = True
while game_is_one:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle right
    if (
        ball.distance(paddle_right) < 50
        and ball.xcor() > 320
        or ball.distance(paddle_left) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.ball_reset()
        Scoreboard.l_point()

    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.ball_reset()
        Scoreboard.r_point()


screen.exitonclick()
