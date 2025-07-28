from turtle import Turtle
L_POSITION = -100
R_POSITION = 100

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(L_POSITION, 240)
        self.write(self.l_score, align='center', font=('Courier', 40, 'bold'))
        self.goto(R_POSITION, 240)
        self.write(self.r_score, align='center', font=('Courier', 40, 'bold'))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()