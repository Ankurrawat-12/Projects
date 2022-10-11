from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
paddle_l = Paddle((-380, 0))
paddle_r = Paddle((380, 0))
ball = Ball()


def boundary__():
    boundary = Turtle()
    boundary.color("white")
    boundary.speed("fastest")
    boundary.hideturtle()
    boundary_ = [(0, -300), (-400, -300), (-400, 300), (400, 300), (400, -300), (0, -300), (0, 300)]
    for i in range(len(boundary_)):
        boundary.goto(boundary_[i])

boundary__()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_l.up_, "w")
screen.onkeypress(paddle_l.down_, "s")
screen.onkey(paddle_r.up_, "Up")
screen.onkey(paddle_r.down_, "Down")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # boundary_ = [(0, -250), (-450, -250), (-450, 250), (450, 250), (450, -250), (0, -250), (0, 250)]
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) <= 50 and ball.xcor() > 320 or ball.distance(paddle_l) <= 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.increase_l_score()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.increase_r_score()
        ball.reset_position()

    if scoreboard.r_score == 5 or scoreboard.l_score == 5:
        is_game_on = False
        scoreboard.game_over()

screen.exitonclick()
