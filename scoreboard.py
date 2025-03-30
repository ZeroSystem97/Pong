from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x_cor, 260)
        self.score = 0
        self.update()


    def update(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Arial", 26, "bold"))