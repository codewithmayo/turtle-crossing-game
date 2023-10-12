from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.update_scoreboard()

    def increase_level(self):
        self.clear()
        self.level += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align="center", font=FONT)

