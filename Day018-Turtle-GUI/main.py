import math
from turtle import Turtle, Screen, colormode, mode
import random
tim = Turtle()

tim.speed("fastest")
tim.pensize(8)
color_m = colormode(255)
mode("logo")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_c = (r, g, b)
    return random_c

# for _ in range(4):
#     tim.forward(25)
#     tim.left(90)
colors = ["red","blue","green","black","magenta","cyan","purple","brown","pink"]
directions = [0, 90, 180, 270]
# def draw_shape (num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(75)
#         tim.right(angle)
#
# for shape_side_n in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)


# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# def draw_shape (num_sides):
#     angles = [90,180,270]
#     angle = random.choice(angles)
#     turns = ["left","right"]
#     turn = random.choice(turns)
#     for _ in range(num_sides):
#         tim.forward(25)
#         tim.left(angle)

# for _ in range(1000):
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())
#     tim.forward(25)

# n = 0
# while n < 36:
#     tim.color(random_color())
#     tim.left(10)
#     tim.circle(90)
#     n += 1

def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()


# import heroes
# print(heroes.gen())

