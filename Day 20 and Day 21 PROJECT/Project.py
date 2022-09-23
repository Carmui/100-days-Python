from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake APP")
screen.tracer(0)

new_snake = Snake()
food = Food()
new_scoreboard = Scoreboard()

screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    new_snake.move()

    # Detect collision with food.
    if new_snake.head.distance(food) < 15:
        new_scoreboard.score += 1
        food.refresh()
        new_snake.extend()
        new_scoreboard.update_score()

    # Detect collision with wall.
    if new_snake.head.xcor() > 280 or new_snake.head.xcor() < -280 or new_snake.head.ycor() > 280 or new_snake.head.ycor() < -280:
        new_scoreboard.game_over()
        game_is_on = False

    # Detect colission with tail.
    for segment in new_snake.segments[1::]:
        if new_snake.head.distance(segment) < 10:
            game_is_on = False
            new_scoreboard.game_over()

screen.exitonclick()
