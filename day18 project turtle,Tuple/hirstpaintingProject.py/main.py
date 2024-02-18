import colorgram
import turtle as t
from turtle import Screen
import random
tatti = t.Turtle()

tatti.shape('turtle')
tatti.color('red')

# hirst_colors = colorgram.extract('image.jpg',30)
# color_list = []
# for color in hirst_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r,g,b)
#     color_list.append(rgb)
# print(color_list)
tatti.hideturtle()
rgb_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
t.colormode(255)
tatti.penup()
tatti.setheading(225)
tatti.forward(250)
tatti.setheading(0)
num_dots = 100 
tatti.speed("fastest")
for dots in range(1, num_dots +1):
    tatti.dot(20 ,random.choice(rgb_list))
    tatti.forward(50)
    if dots % 10 == 0:
        tatti.setheading(90)      
        tatti.forward(50)
        tatti.setheading(180)
        tatti.forward(500) #50 * 10 dots = 500 spaces
        tatti.setheading(0) # to make it face the same direction




        # generally used at last
screen = Screen()
screen.exitonclick()
