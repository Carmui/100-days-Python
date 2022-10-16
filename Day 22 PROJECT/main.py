from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# SET SCREEN
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong APP")
screen.tracer(0)

# SET PADDLES
r_paddle = Paddle(350)
l_paddle = Paddle(-350)

# SET BALL
ball = Ball()

# SET Scoreboard
scoreboard = Scoreboard()

screen.listen()
# GO UP
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(l_paddle.go_up, "w")

# GO DOWN
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    #Detect collision with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # Detect L Paddle misses
    if ball.xcor() < -380:
        scoreboard.p_point()
        ball.reset_position()




screen.exitonclick()
