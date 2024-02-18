from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("black")
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-340,260)
        self.write(f"Level = {self.score +1}", align="center" , font=("Arial" , 15 , "normal"))
    
    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
            self.goto(0,0)
            self.write("Game Over" , align="center" , font=("Arial" , 24 , "normal"))
