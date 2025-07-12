from turtle import Turtle, Screen
screen = Screen()
timmy = Turtle()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_left():
    timmy.left(10)

def turn_right():
    timmy.right(10)

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.textinput("Make your bet", "Who will win? Enter a color:")
screen.listen()
screen.onkey( move_forwards, "w")
screen.onkey( move_backwards, "s")
screen.onkey( turn_left, "a")
screen.onkey( turn_right, "d")
screen.onkey( clear_screen, "c")
screen.exitonclick()
