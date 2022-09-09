from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3

class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            y_pos = random.randint(-250, 250)
            car.goto(x=300, y=y_pos)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.setheading(180)
            car.fd(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT