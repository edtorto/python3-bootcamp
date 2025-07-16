import time
from turtle import Turtle, Screen

# Set the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

starting_position = [(0,0),(-20,0),(-40,0)]

# create three segments of white turtle in a square shape

segments = []
for position in starting_position:
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.color("white")
    new_turtle.shape("square")
    new_turtle.goto(position)
    segments.append(new_turtle)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for seg in range(len(segments)-1, 0, -1):
        new_x = segments[seg - 1].xcor()
        new_y = segments[seg - 1].ycor()
        segments[seg].goto(new_x, new_y)
    segments[0].forward(20)


screen.exitonclick()