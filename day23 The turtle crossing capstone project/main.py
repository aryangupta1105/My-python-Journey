import turtle as t
from car_manager import Cars
from player import Player
from score_board import Score
import time


screen = t.Screen()
screen.setup(height=600 , width= 800)
screen.bgcolor("white")
screen.title("The Turtle Crossing Game")
screen.tracer(0)

game_player = Player()
cars = Cars()
score = Score()

screen.listen()
screen.onkey(key="Up" , fun= game_player.move)
def line(position):
    line = t.Turtle()
    line.hideturtle()
    line.penup()
    line.goto(position)
    line.setheading(180)
    for _ in range(100):
        line.pendown()
        line.forward(10)
        line.penup()
        line.forward(10)

game_on = True
while game_on:
    line((400,-240))
    line((400,240))
    screen.update()
    time.sleep(0.1)
    cars.create_random_cars() 
    cars.move()

    #detecting collisions with cars:
    for car in cars.all_cars:
        if car.distance(game_player) < 20:
            game_on = False
            score.game_over()
    if game_player.is_at_finish() :
        score.increase_score()
        game_player.go_to_start()
        cars.level_up()


    #checking the player has crossed the 
screen.exitonclick()