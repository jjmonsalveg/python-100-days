from question_model import Question


class QuizBrain:
    def __init__(self, question_list: list[Question]):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self) -> None:
        new_question = self.question_list[self.question_number]
        user_answer = input(
            f"Q.{self.question_number + 1}: {new_question.text} (True/False)?:"
        )
        self.question_number += 1
        self.check_answer(user_answer, new_question.answer)

    def still_has_question(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer: str, correct_answer: str):
        if user_answer.casefold() == correct_answer.casefold():
            print("you got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
