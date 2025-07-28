from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

number_of_rounds = int(screen.numinput("Number of Rounds", "How many rounds do you want to play?"))

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()

turtle = Turtle()
turtle.hideturtle()
turtle.color("white")
turtle.penup()
turtle.goto(0, -280)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
rounds_played = 0

game_is_on = True

while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with the ball
    if (ball.distance(r_paddle) < 60 and ball.xcor() > 320
            or ball.distance(l_paddle) < 60 and ball.xcor() < -320):
        ball.bounce_x()

    #Detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        rounds_played += 1

    # Detect L paddle miss
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        rounds_played += 1
    turtle.clear()
    turtle.write(f"Rounds = {rounds_played}", align='center', font=('Courier', 20, 'bold'))

    if number_of_rounds == rounds_played:
        game_is_on = False
        turtle.goto(0, 0)
        turtle.write("GAME OVER!", align='center', font=('Courier', 20, 'bold'))


screen.exitonclick()