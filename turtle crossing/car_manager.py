from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1
CARS = 25
CARS_POSITIONS = [-295, -285, -275, -265, -255, -245, -235, -225, -215, -205, -195, -185, -175, -165, -155, -145, -135,
                  -125, -115, -105, -95, -85, -75, -65, -55, -45, -35, -25, -15, -5, 5, 15, 25, 35, 45, 55, 65, 75, 85,
                  75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275,
                  285, 295, 305, 315, 325, 335, 345, 355, 365, 375, 385, 395]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.make_car()

    def make_car(self):
        for i in range(CARS):
            new_car = Turtle("square")
            new_car.shapesize(1, 1.5, 1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(random.choice(CARS_POSITIONS), random.randint(-260, 280))
            self.cars.append(new_car)

    def move(self):
        for i in range(CARS):
            self.cars[i].backward(STARTING_MOVE_DISTANCE)

    def again(self, i):
        self.cars[i].goto(300, random.randint(-280, 280))

    def faster(self):
        global STARTING_MOVE_DISTANCE, CARS
        for i in range(CARS):
            self.cars[i].goto(random.choice(CARS_POSITIONS), random.randint(-260, 280))
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
