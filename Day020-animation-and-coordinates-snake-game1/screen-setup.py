from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

turtle = Turtle()
turtle.shape("square")
turtle.color("white")



screen.exitonclick()