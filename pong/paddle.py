from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.activate = False
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up_(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 25
            self.goto(self.xcor(), new_y)

    def down_(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 25
            self.goto(self.xcor(), new_y)


