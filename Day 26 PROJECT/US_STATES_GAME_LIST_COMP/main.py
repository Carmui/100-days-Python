import turtle

import pandas
import pandas as pd

# Data import
data = pd.read_csv("50_states.csv")

is_game_on = True
points = 0

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states =[]

all_states = data.state.to_list()

while is_game_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    data_state = data["state"].str.lower()

    if answer_state.lower() == "exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_you_missed")
        break

    if data_state.isin([answer_state.lower()]).any():
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        x_pos = data.loc[data_state == answer_state.lower()]['x'].item()
        y_pos = data.loc[data_state == answer_state.lower()]['y'].item()
        t.goto(int(x_pos), int(y_pos))
        t.write(answer_state.lower())

        guessed_states.append(answer_state.lower())
        points += 1

    if points == 50:
        is_game_on = False



#def get_mouse_click_coor(x, y):
#    print(x, y)
#
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

#screen.exitonclick()