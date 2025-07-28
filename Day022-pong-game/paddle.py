from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle:
    def __init__(self):
        """initialize the paddle"""
        self.segments = []

        self.create_paddle()
        self.head = self.segments[0]

    def create_paddle(self):
        """appends turtle segments to the segments list to create a paddle """
        for position in STARTING_POSITION:
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.shape("square")
            new_turtle.goto(position)
            self.segments.append(new_turtle)

    # def position_paddle(self, x, y):

    def move(self):
        """moves the paddle """
        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        self.segments[0].goto(0, -100)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
