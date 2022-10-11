from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.level_()

    def level_(self):
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.write(f"LEVEL :- {self.level}", align="left", font=FONT)

    def level_changer(self):
        self.level += 1
        self.clear()
        self.level_()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER ", align="center", font=FONT)
