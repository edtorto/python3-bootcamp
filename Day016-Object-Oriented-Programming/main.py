# import another_module
# print(another_module.another_variable)
#
# import turtle # Import module called turtle
#
# tita = turtle.Turtle() # New turtle object called titi of class called Turtle()
from imaplib import Literal

# #  Another way
# from turtle import Turtle, Screen
#
# tite = Turtle()
# tite.shape("turtle")
# tite.color("red")
# print(tite)
# my_screen = Screen()
# tite.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokeman Name", ["Pikachu", "Squirtle", "Chamander"], )
table.add_column("Type", ["Electric", "Water", "Fire",])
table.align = "l"
print(table)
