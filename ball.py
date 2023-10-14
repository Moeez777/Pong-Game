import turtle
from turtle import Turtle,Screen
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x=10
        self.move_y=10
        self.move_speed=0.1
    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)
    def collision_y(self):
        self.move_y*=-1
    def collision_x(self):
        self.move_speed*=0.8
        self.move_x *= -1
    def reverse(self):
        self.goto(0, 0)
        self.collision_x()
        self.move_speed=0.1

