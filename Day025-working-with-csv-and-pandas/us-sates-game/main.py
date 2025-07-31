import turtle

screen = turtle.Screen()
screen.setup(600, 400)
screen.title("U.S. State Game")
image = "blank-states-img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click)
turtle.mainloop()

