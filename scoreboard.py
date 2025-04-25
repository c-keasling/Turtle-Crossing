from turtle import Turtle
FONT = ("Amazon ember", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-240,255)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align="center", font=FONT)


