import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
cars = CarManager()

game_is_on = True
screen.listen()
screen.onkeypress(player.up, "Up")
# screen.onkeypress(player.down, "Down")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.is_finish():
        score.level_changer()
        player.new()
        cars.faster()

    cars.move()
    for i in range(len(cars.cars)):
        if cars.cars[i].xcor() <= -300:
            cars.again(i)
    for i in range(len(cars.cars)):
        if player.distance(cars.cars[i]) <= 20:
            game_is_on = False
            score.game_over()


screen.exitonclick()
