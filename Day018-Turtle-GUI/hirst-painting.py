import random
import turtle as turtle_module
# import colorgram

# tutle documentation
"https://docs.python.org/3/library/turtle.html"

# # Extract 10 colors from an image.
# colors = colorgram.extract('hirst_image.jpg', 10)

# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
# print(color_list)

tim = turtle_module.Turtle()
screen = turtle_module.Screen()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
color_list = [(234, 225, 83), (195, 8, 69), (231, 54, 132), (194, 164, 15), (112, 178, 214), (199, 77, 15)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)


# makes hirst paint using colors extracted from Day018-Turtle-GUI/hirst_image.jpg with colorgram module
num_of_dots = 100
for dot_count in range(1, num_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
