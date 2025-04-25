from tkinter import Tk, Label, Canvas, PhotoImage, Button

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self._quiz_brain = quiz_brain
        self._window = Tk()
        self._window.title("Quizzler")
        self._window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(
            text="Score: 0",
            bg=THEME_COLOR,
            fg="white",
        )
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.true_response
        )
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image, highlightthickness=0, command=self.false_response
        )
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self._window.mainloop()

    def get_next_question(self):
        q_text = self._quiz_brain.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_response(self):
        is_right = self._quiz_brain.check_answer("True")
        self.give_feedback(is_right)
        self.update_score()

    def false_response(self):
        is_right = self._quiz_brain.check_answer("False")
        self.give_feedback(is_right)
        self.update_score()

    def update_score(self):
        score = self._quiz_brain.score
        self.score_label.config(text=f"Score: {score}")

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self._window.after(1000, self.reset_canvas)

    def reset_canvas(self):
        self.canvas.config(bg="white")
        if self._quiz_brain.still_has_questions():
            self.get_next_question()
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the question list"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
