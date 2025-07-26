from turtle import Turtle
import random

class Food(Turtle):# Inherit properties and behaviors of the Turtle class
    def __init__(self):
        """Initialize the inheritance of Turtle class to Food class"""
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Moves the food to random location"""
        random_x = random.randint(-180, 180)
        random_y = random.randint(-180, 180)
        self.goto(random_x, random_y)