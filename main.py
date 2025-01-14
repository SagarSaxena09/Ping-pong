from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Ping Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)

screen.onkey(key="s", fun=l_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score()

screen.exitonclick()