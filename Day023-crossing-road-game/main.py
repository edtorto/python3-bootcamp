import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

#Set the screen
screen.setup(width=800, height=600)
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

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect successful crossing
    if player.is_at_finish_line():
        player.move_to_the_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()