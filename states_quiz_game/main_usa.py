import turtle
import pandas

ALIGN = "center"
FONT = ("Arial", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725, 491)
image = "states_quiz_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_cordinate(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cordinate)
states_data = pandas.read_csv("./states_quiz_game/50_states.csv")
all_states = states_data["state"].tolist()

game_is_on = True
guessed_states = []
while len(guessed_states) <= 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another name state's name?",
    )

    if answer_state is None or answer_state.lower() == "exit":
        missed_states = []
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("./states_quiz_game/states_to_learn.csv")
        break

    if answer_state is not None:
        state_name = answer_state.title()
        if state_name in all_states:
            guessed_states.append(state_name)
            state = states_data[states_data["state"] == state_name]
            show_state = turtle.Turtle()
            show_state.penup()
            show_state.hideturtle()
            show_state.goto(state["x"].item(), state["y"].item())
            show_state.write(f"{state_name}", False, align=ALIGN, font=FONT)

turtle.mainloop()
