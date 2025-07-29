from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.high_score = self.read_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} HighScore {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score()
        self.score = 0
        self.update_scoreboard()

    def read_score(self):
        with open("data.txt") as self.h_score:
            h_score = int(self.h_score.read())
            return h_score

    def write_score(self):
        with open("data.txt", "w") as self.f:
            self.f.write(str(self.high_score))
