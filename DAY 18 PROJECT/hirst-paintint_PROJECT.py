import turtle as t
import colorgram
import random

joko = t.Turtle()
rgb_colors = []
colors = colorgram.extract('spot_paint.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tupler = (r, g, b)
    rgb_colors.append(tupler)

joko.penup()
joko.setheading(225)
joko.forward(400)
joko.setheading(0)

number_of_dots = 15
number_of_lines = 5

for j in range(number_of_lines):
    for i in range(number_of_dots):
        joko.pendown()
        t.colormode(255)
        joko.dot(20, random.choice(rgb_colors))
        joko.penup()
        joko.forward(50)

    if j % 2 == 0:
        joko.setheading(90)
        joko.forward(50)
        joko.setheading(180)
        joko.forward(50)
    else:
        joko.setheading(90)
        joko.forward(50)
        joko.setheading(0)
        joko.forward(50)


screen = t.Screen()
screen.exitonclick()
