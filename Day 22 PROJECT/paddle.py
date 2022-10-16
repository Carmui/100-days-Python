from turtle import Turtle, Screen

Y_COR = 0

class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.color("white")
        self.goto(x_cor, Y_COR)

    def go_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)
