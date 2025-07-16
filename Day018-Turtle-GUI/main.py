from turtle import Turtle, Screen, colormode
import random
tim = Turtle()

tim.speed("fastest")
tim.pensize(8)
color_m = colormode(255)

def random_color():
    """Returns a tuple representing a random color of RGB."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_c = (r, g, b)
    return random_c

# Draws a triangle
for _ in range(4):
    tim.forward(25)
    tim.left(90)

colors = ["red","blue","green","black","magenta","cyan","purple","brown","pink"]
directions = [0, 90, 180, 270]

def draw_shape (num_sides):
    """Draws shapes from triangle to decagon with different colors."""
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(75)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

# Draws dotted lines
for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# Makes a random walk of turtle with multiple colors
for _ in range(1000):
    tim.setheading(random.choice(directions))
    tim.color(random_color())
    tim.forward(25)

# Draws a spirograph
# n = 0
# while n < 36:
#     tim.color(random_color())
#     tim.left(10)
#     tim.circle(90)
#     n += 1

def draw_spirograph(gap_size):
    """Draws a spirograph of size gap_size."""
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()

# Prints heroes names
import heroes
print(heroes.gen())

