from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-290, 250)
        self.level = 1
        self.score_write()

    def score_write(self):
        self.write(f"Level:{self.level}", False, "left", ("Courier", 25, "normal"))


    def level_up(self):
        self.level+=1
        self.clear()
        self.score_write()

    def game_over(self):
        self.home()
        self.write("GAME OVER", False, "center", ("Courier", 25, "normal" ))






