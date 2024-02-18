import turtle as t 
MOVE_DISTANCE = 20
starting_position = ((0,0),(-20,0),(-40,0))
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake :

    def __init__(self):
        self.snake_body_parts = []
        self.create_snake()
        self.head = self.snake_body_parts[0]


    def create_snake(self):
        for position in starting_position:
            self.add_part(position)


    def move(self):
        for num in range(len(self.snake_body_parts)-1, 0 , -1):
            new_x = self.snake_body_parts[num-1].xcor()
            new_y = self.snake_body_parts[num-1].ycor()
            self.snake_body_parts[num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_part(self , position):
        self.snake_body = t.Turtle("square")
        self.snake_body.color("white")
        self.snake_body.penup()
        self.snake_body.goto(position)
        self.snake_body_parts.append(self.snake_body)
    
    def grow(self):
        self.add_part(self.snake_body_parts[-1].position())

    def reset(self):
        for part in self.snake_body_parts:
            part.goto(1000,1000)
        self.snake_body_parts.clear()
        self.create_snake()
        self.head = self.snake_body_parts[0]

            
        

