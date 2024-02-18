import tkinter as t
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self , quiz_brain):
        self.quiz = quiz_brain
        self.window = t.Tk()
        self.window.title("The Quizzler")
        self.window.config(padx=20 , pady=20 ,bg=THEME_COLOR)

        # Creating canvas
        self.canvas = t.Canvas(height=250 , width=300)
        self.q_text = self.canvas.create_text(150 , 125 , text="", font=("Arial", 20 , "italic") ,fill="black" ,width=280)
        self.canvas.grid(row=1 , column=0 ,columnspan=2)

        #creating score label
        self.score = t.Label()
        self.score.config(text=f"Score:{self.quiz.score}" , bg=THEME_COLOR, fg="white" , font=("Arial",10,"normal") , pady=50)
        self.score.grid(row=0 , column=1)

        #creating buttons
        right_img = t.PhotoImage(file="day34 Quizzler and Api/002 quizzler-app-start/images/true.png")
        wrong_img = t.PhotoImage(file="day34 Quizzler and Api/002 quizzler-app-start/images/false.png")

        right_button = t.Button() 
        right_button.config(image=right_img , pady=50 , command=self.is_true)
        right_button.grid(row=2 , column=0 )

        wrong_button = t.Button() 
        wrong_button.config(image=wrong_img  , pady=50 , command=self.is_false)
        wrong_button.grid(row=2 , column=1  )


        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text , text=question)
        else:
           self.canvas.itemconfig(self.q_text  , text="The quiz has completed.")
           self.right_button.config(state="disabled")
           self.wrong_button.config(state="disabled")

    def is_true(self):
        is_right =  self.quiz.check_answer("True")
        self.give_feedback(is_right)
        # if is_right:
        #     self.canvas.config(bg="green")
        # else:
        #     self.canvas.config(bg="red")
        # self.canvas.config(bg="white")
        # self.next_question()
        
        
    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self , is_right):
        if is_right:
            self.score.config(text=f"Score:{self.quiz.score}" , bg=THEME_COLOR, fg="white" , font=("Arial",10,"normal") , pady=50)
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        feedback_timer = self.window.after(1000 , self.next_question)





