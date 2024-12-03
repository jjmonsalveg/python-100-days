from tkinter import Button, Entry, Label, Tk


def button_clicked():
    miles = float(miles_input.get())
    km = miles * 1.60934
    result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

window.mainloop()
