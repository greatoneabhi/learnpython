import turtle
import pandas

ALIGN = "center"
FONT = ("Arial", 10, "bold")

screen = turtle.Screen()
screen.title("Guess states")
image = "./states_quiz_game/india_map.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_cordinates(x, y):
    print(x, y)


screen.onscreenclick(get_mouse_click_cordinates)

states_data = pandas.read_csv("./states_quiz_game/india_states.csv")
all_states = states_data["state"].tolist()

states_correct = 0
is_game_on = True
while is_game_on:
    if states_correct == 0:
        answer_state = screen.textinput(
            title="Guess the state", prompt="What's another name state's name?"
        )
    else:
        answer_state = screen.textinput(
            title=f"{states_correct}/32 States Correct",
            prompt="What's another name state's name?",
        )
    if answer_state is None:
        is_game_on = False

    if answer_state is not None and answer_state.title() in all_states:
        states_correct += 1
        state = states_data[states_data["state"] == answer_state.title()]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        x_cord = state["x"].item()
        y_cord = state["y"].item()
        t.goto(x_cord, y_cord)
        t.write(f"{state["state"].item()}", False, align=ALIGN, font=FONT)

turtle.mainloop()
