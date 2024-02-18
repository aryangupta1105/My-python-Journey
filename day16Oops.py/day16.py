from turtle import Turtle, Screen
import another
# print(another.another_var)
# tattu = Turtle()
# print(tattu)
# tattu.forward(100)
# tattu.left(100)
# tattu.forward(100)
# tattu.shape('turtle')
# tattu.color('pink')
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("City_name",[
    'Dabra','Gwalior',"Bhopal","Indore","Satna","Vidisha","Rewa"
])
table.align = "l"

#addcolumns is used to make column in the table
#It takes heading and list of data
table.add_column("num_visits",[12,3,23,43,53,12,3])
print(table)

