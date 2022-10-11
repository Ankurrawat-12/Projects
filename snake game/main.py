import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
boundarys = [(-300, -300), (300, -300), (300, 300), (-300, 300), (-300, -300)]
boundary = Turtle()
boundary.hideturtle()
boundary.color("white")
boundary.pensize(15)
boundary.penup()
boundary.goto(-300, 300)
boundary.pendown()
for i in range(len(boundarys)):
    boundary.goto(boundarys[i])

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkeypress(snake.pause_play, 'space')
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    if snake.activate:
        snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
