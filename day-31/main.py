import random
from tkinter import Button, Canvas, PhotoImage, Tk

import pandas

BACKGROUND_COLOR = "#B1DDC6"


def load_data():
    try:
        new_words = pandas.read_csv("data/words_to_learn.csv")
        return new_words
    except FileNotFoundError:
        new_words = pandas.read_csv("data/french_words.csv")
        return new_words


def flip_card():
    global new_card
    canvas.itemconfig(background_img, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=new_card["English"], fill="white")


def set_new_word():
    global new_card
    global timer_id

    if timer_id:
        window.after_cancel(timer_id)

    new_card = random.choice(data_dict)
    canvas.itemconfig(background_img, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=new_card["French"], fill="black")
    timer_id = window.after(3000, flip_card)


def remove_word():
    data_dict.remove(new_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv")


data = load_data()
data_dict = data.to_dict(orient="records")
new_card = {}
timer_id = None

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# also canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR) is possible
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
background_img = canvas.create_image(401, 263, image=front_img)
card_title = canvas.create_text(
    400, 150, text="", fill="black", font=("Arial", 40, "italic")
)
card_word = canvas.create_text(
    400, 263, text="", fill="black", font=("Arial", 60, "bold")
)
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=set_new_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(
    image=right_image,
    highlightthickness=0,
    command=lambda: [remove_word(), set_new_word()],
)
right_button.grid(row=1, column=1)

set_new_word()
window.mainloop()
