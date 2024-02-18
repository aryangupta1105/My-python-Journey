import turtle as t
from turtle import Screen
import random
tatti = t.Turtle()

tatti.shape('turtle')
tatti.color('red')

#Draw Dashed line: 

def dashed_line():
    for _ in range(30):
        tatti.forward(10)
        tatti.penup()
        tatti.forward(10)
        tatti.pendown()

dashed_line()



#shapes generator turtle exercise:

# for _ in range(15):
#     tatti.forward(10)
#     tatti.penup()
#     tatti.forward(10)
#     tatti.pendown()
# def draw(num_sides): 
#     color_shape = random.choice(color_list)
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tatti.color(color_shape)
#         tatti.forward(100)
#         tatti.right(angle)
# for n in range(3,11):
#     draw(n)



#random Walk Exercise: 

# color_list = ['aquamarine','pale green','red', 'blue','green','grey', 'chocolate','pink']
# direction = [0,90,180,270]
# def random_walk():
#     tatti.width(10)
#     tatti.speed('fastest')
#     while 3>2:
#         r_color = random.choice(color_list)
#         new_direction = random.choice(direction)
#         tatti.color(r_color)
#         tatti.forward(20)
#         tatti.right(new_direction)
# random_walk()


#tuples and colormode(its a tuple with chooses color in pencolor method):
# direction = [0,90,180,270]
# t.colormode(255)


#Exercise: Spirograph maker:

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     rgb = (r,g,b)
    # return rgb

# tatti.pensize(10)
# tatti.speed('fastest')
# while 3>2:
#     for _ in range(0, 361 , 2):
        # tatti.color(random_color())
        # tatti.right(_)
        # tatti.circle(100,360)

#Method 2:
# def draw_spirograph(gap_size):
#     for _ in range(int(360/gap_size)):
#         tatti.color(random_color())
#         tatti.circle(100,360)
#         current_heading = tatti.heading() #it gives the tilt of the turtle
#         tatti.setheading(current_heading + gap_size) #it sets the tilt of the turtle

# draw_spirograph(5)
# import heroes
# print(heroes.gen())







































#to keep the screen pause for some time:
#generally used at last
screen = Screen()
screen.exitonclick()