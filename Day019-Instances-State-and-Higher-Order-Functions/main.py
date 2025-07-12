from turtle import Turtle, Screen
screen = Screen()
timmy = Turtle()

def move_forwards():
    timmy.forward(10)

screen.listen()
screen.onkey( move_forwards, "space")
screen.exitonclick()
