from turtle import Turtle, Screen
from paddle import Paddle
import time

screen = Screen()
turtle = Turtle()
# Set the screen
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")

turtle.goto(0,-300)
turtle.color("white")
turtle.pensize(5)
turtle.hideturtle()
turtle.left(90)
turtle.speed("fastest")
screen.tracer(0)

# Draws dotted lines
for _ in range(30):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
screen.update()

# Create an instance of a class
paddle = Paddle()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()

# Create an instance of a class
# scoreboard = Scoreboard()

screen.exitonclick()