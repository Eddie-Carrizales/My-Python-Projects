# Author:      Eddie F. Carrizales
# Date:        06/12/2022
# Description: Quiz Creator: This program creates a quiz using question data that is given. The program
# will grab the data and using the question model, the "QuizBrain" will create a quiz the user can take
# as well as provide a score

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# initialize question bank list
question_bank = []

# loop to create a new question object from the text and answer strings in the data.py file
# this new question object will be appended to create a question bank
for i in range(len(question_data)):
    new_question = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(new_question)

# Create a new quiz object by passing the question_bank
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    # Will call the next_question method to show the question in the quiz
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")