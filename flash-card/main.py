from tkinter import Button, Canvas, PhotoImage, Tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
flip_timer = None
current_card = {}

try:
    data = pandas.read_csv("./flash-card/data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./flash-card/data/french_words.csv")

to_learn = data.to_dict(orient="records")


def is_known():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("./flash-card/data/words_to_learn.csv", index=False)
    next_card()


def is_not_known():
    next_card()


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    global flip_timer
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    if flip_timer:
        window.after_cancel(flip_timer)


# --------------------------------------- GUI -----------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./flash-card/images/card_front.png")
card_back_image = PhotoImage(file="./flash-card/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=FONT_TITLE)
card_word = canvas.create_text(400, 263, text="Word", font=FONT_WORD)
canvas.grid(row=0, column=0, columnspan=2)

right_btn_img = PhotoImage(file="./flash-card/images/right.png")
right_btn = Button(
    image=right_btn_img,
    highlightthickness=0,
    border=0,
    bg=BACKGROUND_COLOR,
    command=is_known,
)
right_btn.grid(row=1, column=1)

wrong_btn_img = PhotoImage(file="./flash-card/images/wrong.png")
wrong_btn = Button(
    image=wrong_btn_img,
    highlightthickness=0,
    border=0,
    bg=BACKGROUND_COLOR,
    command=is_not_known,
)
wrong_btn.grid(row=1, column=0)

next_card()

window.mainloop()
