import turtle as t
import random
move_distance = 10
move_increment = 10
color_list =  ['red','orange','yellow','green','blue','purple']
class Cars:


    def __init__(self):
        self.all_cars = []
        self.move_speed = move_distance
        

        
    def create_random_cars(self):
        self.random_chance = random.randint(1,6)
        if self.random_chance == 1:
            self.color_chosen = random.choice(color_list)
            self.new_car = t.Turtle()
            self.new_car.shape("square")
            self.new_car.shapesize(stretch_len= 2 ,stretch_wid=1)
            self.new_car.penup()
            self.new_car.color(self.color_chosen)
            self.random_y = random.randint(-240 , 240)
            self.new_car.goto(340 , self.random_y)
            self.all_cars.append(self.new_car)

    def move(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.move_speed)
    
    def level_up(self):
        self.move_speed += move_increment
            

