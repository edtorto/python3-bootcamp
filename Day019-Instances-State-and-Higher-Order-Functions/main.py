from turtle import Turtle, Screen
import random
screen = Screen()
# timmy = Turtle()

# def move_forwards():
#     timmy.forward(10)
#
# def move_backwards():
#     timmy.backward(10)
#
# def turn_left():
#     timmy.left(10)
#
# def turn_right():
#     timmy.right(10)
#
# def clear_screen():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()
#

# screen.listen()
# screen.onkey( move_forwards, "w")
# screen.onkey( move_backwards, "s")
# screen.onkey( turn_left, "a")
# screen.onkey( turn_right, "d")
# screen.onkey( clear_screen, "c")

is_race_on = False
screen.setup(width=800, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "orange", "indigo", "violet"]
y_position = [-70, -40, -10, 20, 50, 80, 110]

all_turtles = []
for turtle_index in range(0, len(y_position)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-390, y=y_position[turtle_index])
        all_turtles.append(new_turtle)

if user_bet:
        is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 370:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
