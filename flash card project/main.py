from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "Python Modules"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv(f"data/{LANGUAGE}_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(f"data/{LANGUAGE}.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_language, text=LANGUAGE, fill="black")
    canvas.itemconfig(card_word, text=current_card[LANGUAGE], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_image)


def is_known():
    to_learn.remove(current_card)
    data_to_learn = pandas.DataFrame(to_learn)
    data_to_learn.to_csv(f"data/{LANGUAGE}_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=20, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=400, height=264, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(200, 132, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)
card_language = canvas.create_text(200, 75, text="", font=("ariel", 20, "italic"))
card_word = canvas.create_text(200, 132, text="", font=("ariel", 10, "bold"), width=380)
# Button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known, bd=0)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card, bd=0)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()

