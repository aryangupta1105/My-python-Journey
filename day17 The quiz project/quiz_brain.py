import random
class Quiz:
    def __init__(self , question_list):
        self.question_list = question_list
        self.num_question = 0
        self.score = 0
        
    def still_has_questions(self):
        return self.num_question < len(self.question_list)
            
    def check_answer(self,user_answer,correct_answer):
        if correct_answer.lower() == user_answer:
            self.score += 1
            print("You got it right!")
            print(f"Your current score is: {self.score}/{self.num_question}")
        else:
            print("That's wrong answer!")
        print(f"The correct answer was {self.correct_answer}")

    def next_question(self):
        self.current_question = self.question_list[self.num_question]
        self.num_question += 1
        self.user_answer = input(f"Q.{self.num_question}: {self.current_question.question} : 'True' or 'False': ").lower()
        self.check_answer(self.user_answer , self.current_question.answer)

    

