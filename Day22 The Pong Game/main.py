import turtle as t
from Pong import Pongs
from ball import Ball
from score_board import Score
import time



screen = t.Screen()
screen.setup(height= 600 , width= 800)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)
l_paddle = Pongs((-350, 0))
r_paddle = Pongs((350 , 0))
game_ball = Ball()
score = Score()
screen.listen()
screen.onkey(key="w", fun= l_paddle.move_up)
screen.onkey( key="s" , fun= l_paddle.move_down)
screen.onkey(key="Up" , fun= r_paddle.move_up)
screen.onkey(key="Down" , fun= r_paddle.move_down)
def create_divider():
        divider = t.Turtle("turtle")
        t.hideturtle()
        divider.goto(x = 0,y = -280)
        divider.color("white")
        divider.setheading(90)
        for new_y in range(30):
            divider.pendown()
            divider.forward(10)
            divider.penup()
            divider.forward(10)

game_on = True
create_divider()
while game_on:
    
    screen.update()
    time.sleep(game_ball.move_speed)
    game_ball.move()

    #detecting collision at walls:
    if game_ball.ycor() < -280 or game_ball.ycor() > 280 :
        game_ball.bounce_y()

    #detect collision with paddles:
    if  (game_ball.xcor() > 320 and game_ball.distance(r_paddle.paddle) < 50)or  (game_ball.xcor() < -320 and game_ball.distance(l_paddle.paddle) < 50) :
        game_ball.bounce_x()


    #checking score:
    if game_ball.xcor() > 380  :
        score.l_point()
        game_ball.refresh()
    if game_ball.xcor() < -380 :
        score.r_point()
        game_ball.refresh()
    

    














screen.exitonclick()