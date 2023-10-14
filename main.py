from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen=Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
r_paddle=Paddle((350, 0))
l_paddle=Paddle((-350, 0))
pong_ball=Ball()
score=Score()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
game_on=True
while game_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move()
    if pong_ball.ycor() > 280 or pong_ball.ycor()<-280:
        pong_ball.collision_y()
    if pong_ball.distance(r_paddle)< 50 and pong_ball.xcor()>320 or pong_ball.distance(l_paddle)< 50 and pong_ball.xcor()<-320:
        pong_ball.collision_x()
    if pong_ball.xcor()>380:
        pong_ball.reverse()
        score.l_point()
    if pong_ball.xcor()<-380:
        pong_ball.reverse()
        score.r_point()






screen.exitonclick()