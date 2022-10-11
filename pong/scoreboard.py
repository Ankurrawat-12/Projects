
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        self.l_score = 0
        self.r_score = 0
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.l_score} {self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        if self.l_score == 5:
            self.goto(0, 0)
            self.write(f"GAME OVER LEFT SIDE PLAYER WON", align=ALIGNMENT, font=FONT)
        else:
            self.goto(0, 0)
            self.write(f"GAME OVER RIGHT SIDE PLAYER WON", align=ALIGNMENT, font=FONT)
