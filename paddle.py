from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,direction):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(5, 1)
        self.penup()
        self.goto(direction)
    def up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(), new_y)
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)