from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

turtle1 = Turtle()
turtle1.shape("square")

turtle1.color("white")
turtle1.goto(x=0, y=0)

turtle2 = Turtle()
turtle2.shape("square")
turtle2.color("white")
turtle2.goto(x=20, y=0)

turtle3 = Turtle()
turtle3.shape("square")
turtle3.color("white")
turtle3.goto(x=40,y=0)

screen.exitonclick()