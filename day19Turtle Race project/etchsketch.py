import turtle as t

tim = t.Turtle()
screen = t.Screen()
def draw_forward():
    tim.forward(10)
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def  draw_backward():
    tim.backward(10)
def counter_clockwise():
    heading = tim.heading()
    tim.setheading(heading - 10)
def clockwise():
    heading = tim.heading()
    tim.setheading(heading + 10)

def etchSketch():
    screen.listen()
    screen.onkey(key = 'w',fun = draw_forward)
    screen.onkey(key = 's',fun = draw_backward)
    screen.onkey(key = 'a',fun = counter_clockwise)
    screen.onkey(key = 'd',fun = clockwise)
    screen.onkey(key = 'c',fun = clear_drawing)
    screen.exitonclick()


etchSketch()
