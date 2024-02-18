from data import question_data
import random
from question_model import Question
from quiz_brain import Quiz

question_bank = []
for question in question_data:
    new_question = question["question"]
    answer = question["correct_answer"]
    new_question = Question(new_question,answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    print("\n")

print("Wow! You've completed the quiz")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")
