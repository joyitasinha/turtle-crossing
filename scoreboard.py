from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-280, 250)
        self.update_scoreBoard()

    def update_scoreBoard(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def update(self):
        self.level += 1
        self.update_scoreBoard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
