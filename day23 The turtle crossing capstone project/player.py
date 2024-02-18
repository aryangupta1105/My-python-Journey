from turtle import Turtle
move_distance = 10
starting_position = (0,-280)
start_heading = 90
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(start_heading)
        self.penup()
        self.goto(starting_position)

    def move(self):
        self.forward(move_distance)

    def is_at_finish(self):
        return self.ycor() >240

    def go_to_start(self):
        self.goto(starting_position)