#####Turtle Intro######

import turtle as t
import heroes
import random as r

timmy_the_turtle = t.Turtle()

#timmy_the_turtle.color("red")
#timmy_the_turtle.forward(100)
#timmy_the_turtle.backward(200)
#timmy_the_turtle.right(90)
#timmy_the_turtle.left(180)
#timmy_the_turtle.setheading(0)
#timmy_the_turtle.shape("turtle")

timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

######## Challenge 1 - Draw a Square ############
for i in range(4):
    timmy_the_turtle.forward(150)
    timmy_the_turtle.right(90)

timmy_the_turtle.clear()

######## Challenge 2 - Draw a dotted line ############
for i in range(5):
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(50)
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(50)

timmy_the_turtle.reset()

timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

######## Challenge 3 - Draw a dotted line ############
for i in range(3, 10):
    timmy_the_turtle.pendown()
    for j in range(i):
        angle = 360/i
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

timmy_the_turtle.reset()

timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

######## Challenge 4 - Random walk ############

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

directions = [0, 90, 180, 270, 360]

for i in range(30):
    timmy_the_turtle.color(r.choice(colours))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(r.choice(directions))

timmy_the_turtle.reset()

######## Challenge 5 - Spiro ############

t.colormode(255)

def random_color():
    er = r.randint(0, 255)
    g = r.randint(0, 255)
    b = r.randint(0, 255)
    color = (er, g, b)
    return color

timmy_the_turtle.speed("fastest")

for i in range(100):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.setheading(timmy_the_turtle.heading() + 10)


screen = t.Screen()
screen.exitonclick()