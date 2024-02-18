from turtle import Turtle
ALIGNMENT = "center" 
FONT =("Arial",15, "normal")
with open("data.txt") as score_file:
    highscore = score_file.read()
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(highscore)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x = 0 , y = 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score = {self.score}   High Score: {self.high_score}",move = False , align = ALIGNMENT ,font = FONT)
    
    def increase_score(self):
        self.score += 1
        self.update()
        

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over! Click 'R' to play again!",move = False , align = ALIGNMENT ,font = FONT)
        
    def reset(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            with open('data.txt' , mode='w') as highscore:
                highscore.write(f"{self.high_score}")

        self.score = 0
        self.update()


        
