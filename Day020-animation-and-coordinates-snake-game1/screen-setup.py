from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

starting_position = [(0,0),(-20,0),(-40,0)]

for position in starting_position:
    new_turtle = Turtle()
    new_turtle.color("white")
    new_turtle.shape("square")
    new_turtle.goto(position)

screen.exitonclick()