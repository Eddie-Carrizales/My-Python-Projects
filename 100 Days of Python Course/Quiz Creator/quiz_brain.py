
# class used to initialize our quizzes attributes, go to the next question in the quiz
# determine if we still have questions in the quiz, and check if the answer the user entered was correct
class QuizBrain:

    # Constructor to create attributes and initialize the question_number
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    # Method to show the current question to the user and receive their input
    def next_question(self):
        # pull the question form the list depending on which question number we are on
        current_question = self.questions_list[self.question_number]

        # Increasing the current question number otherwise it will only show zero
        self.question_number += 1

        # Show the user the question number and the text of the current question.
        # NOTE: We accessed the current_question attribute text, without that it would show us the objects address
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        return False

    def check_answer(self, user_ans, correct_ans ):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_ans}")
        print(f"Your current score is: {self.score}/{self.question_number} \n")
