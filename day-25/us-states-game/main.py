import turtle
import pandas

ALIGNMENT = "CENTER"
FONT = ("Courier", 12, "normal")
NUMBER_OF_STATES_OF_AMERICA = 50

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
count_guess = 0
guessed_states = []

while count_guess < NUMBER_OF_STATES_OF_AMERICA:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

    data = pandas.read_csv("50_states.csv")

    if answer_state == "Exit":
        missing_states = []
        for state in data.state.values:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in data.state.values:
        guessed_states.append(answer_state)
        count_guess += 1
        screen.title(f"{count_guess}/50 States Correct")
        found_state = data[data.state == answer_state]

        state_ui = turtle.Turtle()
        state_ui.penup()
        state_ui.hideturtle()
        state_ui.goto(found_state.x.item(), found_state.y.item())
        state_ui.write(answer_state.title(), True, align=ALIGNMENT, font=FONT)

screen.exitonclick()