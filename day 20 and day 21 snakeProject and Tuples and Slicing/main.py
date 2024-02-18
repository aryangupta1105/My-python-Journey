import turtle as t
import random
import time
from  Snakeclass import Snake
from food import Food
from score_board import Scoreboard

#Turning off the tracer so we can use the update method when needed.......

screen = t.Screen()
def snake_game():
    screen.clear()
    screen.setup(height = 600 , width = 600)
    screen.bgcolor("green")
    #It is used to set background color of the screen
    screen.title("Snake Game")
    #dimension of the turtle is 20x20

    screen.tracer(0) #part of "animation control".....
    snake = Snake()
    food = Food()
    score = Scoreboard()

    screen.listen()
    screen.onkey(key="Up" , fun= snake.up)
    screen.onkey(key="Down" , fun= snake.down)
    screen.onkey(key="Left" , fun= snake.left)
    screen.onkey(key="Right" , fun= snake.right)
    screen.onkey(key="r" , fun = snake_game)
    game_on = True
    while game_on: 
        #very important 
        screen.update()
        #so that it will update only after whole segment are moved 20 spacess...
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) <15: #turtle.distance() method is used to check the distance from turtle
            food.refresh() 
            snake.grow()
            score.increase_score()
        #Detecting collision with walls
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            score.reset()
            snake.reset()
        #Detecting collision with its own tail:
        for parts in snake.snake_body_parts[1:]:
            if snake.head.distance(parts) < 10: 
                score.reset()
                snake.reset()
       

            
snake_game()
    # snake_body_parts[0].right(90)
        #but the segments look like shit so 
        #WE WILL USE TRACER METHOD OF TURTLE GRAPHICS

screen.exitonclick()