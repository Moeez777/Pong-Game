from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score=0
        self.l_score=0
        self.update()
    def update(self):
        self.clear()
        self.goto(-100,190)
        self.write(self.l_score,False,"center",("Courier",88,"normal"))
        self.goto(100,190)
        self.write(self.r_score,False,"center",("Courier",88,"normal"))
    def l_point(self):
        self.l_score+=1
        self.update()
    def r_point(self):
        self.r_score+=1
        self.update()

