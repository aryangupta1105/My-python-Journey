import turtle as t 
class Pongs:

    def __init__(self , position):
        self.create_paddle(position)
        self.score = 0

    def create_paddle(self,position):
        self.paddle = t.Turtle("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_len=1 , stretch_wid= 5)
        self.paddle.penup() 
        self.paddle.goto(position)
    

    def move_up(self):
        self.new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor() ,self.new_y)
        
    def move_down(self):
        self.new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor() ,self.new_y)
        
        
