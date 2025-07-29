import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

#Set the screen
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('white')
screen.title('Crossing Road Game')

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#Move the turtle with keypress
screen.listen()
screen.onkey(player.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #create and move cars
    car_manager.create_car()
    car_manager.move_cars()

screen.exitonclick()