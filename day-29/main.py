from random import choice, randint, shuffle
from tkinter import END, Button, Canvas, Entry, Label, PhotoImage, Tk, messagebox

import pyperclip

FONT_NAME = "Courier"
FONT_SIZE = 14
DEFAULT_EMAIL = "angela@gmail.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    letters = [choice(letters) for _ in range(randint(8, 10))]
    numbers = [choice(numbers) for _ in range(randint(2, 4))]
    symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letters + numbers + symbols

    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password )

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save() -> None:
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not password or not email:
        messagebox.showwarning(title="Oops",message="Please don't leave any fields empty!")
        return
    
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                           f"\n Password: {password}\n Is it ok to save?")

    if is_ok:
        with open("data.txt", mode="a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, DEFAULT_EMAIL)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
photo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, FONT_SIZE))
website_label.grid(column=0, row=1)

website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE))
email_label.grid(column=0, row=2)

email_entry = Entry(width=39)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, DEFAULT_EMAIL)

password_label = Label(text="Password:", font=(FONT_NAME, FONT_SIZE))
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command= generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()