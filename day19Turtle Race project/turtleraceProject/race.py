import turtle as t
import random

race_on = False

screen = t.Screen()
screen.setup(width = 500, height = 400) 
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race?")
print(user_bet)
colors = ['red','orange','yellow','green','blue','purple']
x = -230  
y = -100  
turtle_list = []
for color in colors:
    new_turtle = t.Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x,y)
    turtle_list.append(new_turtle)
    y += 50
if user_bet:
    race_on = True

while race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won the bet. The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost the bet. The {winning_color} turtle is the winner.")

        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()



        