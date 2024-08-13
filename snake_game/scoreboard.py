from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.display_score()

    def display_score(self):
        self.clear()
        self.read_high_score()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            False,
            align=ALIGNMENT,
            font=FONT,
        )

    def read_high_score(self):
        with open("snake_game/high_score.txt") as file:
            content = file.read()
            if content is not None and content != "":
                self.high_score = int(content)

    def update_high_score(self):
        with open("snake_game/high_score.txt", mode="w") as file:
            file.write(str(self.high_score))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.display_score()

    def update(self):
        self.score = self.score + 1
        self.display_score()
