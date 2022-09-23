from tkinter import PhotoImage
from turtle import Turtle, Screen, Shape
import random

screen = Screen()

### Register pokemon images to the screen
images = ['gengar', 'garchomp', 'tyranitar']
for image in images:
    pokemon = PhotoImage(file=f"{image}.gif").subsample(3, 3)
    screen.addshape(f"{image}", Shape("image", pokemon))

screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which pokemon will win the race? Enter a name: ")
y_positions = [-100, 0, 100]
print(user_bet)

all_pokemons = []

for pokemon in range(0, 3):
    new_pokemon = Turtle(images[pokemon])
    new_pokemon.penup()
    new_pokemon.goto(x=-200, y=y_positions[pokemon])
    all_pokemons.append(new_pokemon)

if user_bet:
    is_race_on = True

while is_race_on:
    for pok in range(0, 3):
        if all_pokemons[pok].xcor() > 230:
            is_race_on = False
            winner = images[pok]
            if winner == user_bet:
                print(f"You have won!. The winner is {winner}!")
            else:
                print(f"You have lost! The winner is {winner}")

        random_distance = random.randint(1, 40)
        all_pokemons[pok].forward(random_distance)

screen.exitonclick()