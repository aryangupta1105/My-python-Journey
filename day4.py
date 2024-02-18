# day 4:-
# import random
# choose = str(input("Do you want to flip a coin? Y or N\n"))
# n = random.randint(0,1)
# if choose == 'Y':
#     if n == 0:
#         print("Tails")
#     else:
#         print("Heads")
# elif choose == 'N':
#     print("Thanks for using!!")

# else:
#     print("Invalid Input!!\nThanks for using.")


# import random
# print("Welcome to choose the person pay bill helper:")
# name = input("Give me Everybody's name:- seperated each by', '\n")
# names = name.split(", ")
# n = random.randint(0,(len(names)-1))
# print(names[n],"is lucky enough to pay for the meal!!")

# import random
# print("Welcome to choose the person pay bill helper:")
# name = input("Give me Everybody's name:- seperated each by', '\n")
# names = name.split(", ")
# n = random.choice(names)
# print(n,"is lucky enough to pay for the meal!!")

# Where hide the treasure:
# row1 = ['😀','😅','😂']
# row2 = ['😁','😉','🙂']
# row3 = ['😋','😊','😇']
# map = [row1,row2,row3]
# print(row1)
# print(row2)
# print(row3)
# row = int(input("Where do you want to hide the treasure?\nrow:-"))
# column= int(input("column-"))

# if row == 1:
#     if column == 1:
#         row1[0] = 'x'
#     elif column == 2:
#         row1[1] = 'x'
#     elif column == 3:
#         row1[2] = 'x'
#     else:
#         print("Couldn't hide invalid input!")
# if row == 2:
#     if column == 1:
#         row2[0] = 'x'
#     elif column == 2:
#         row2[1] = 'x'
#     elif column == 3:
#         row3[2] = 'x'
#     else:
#         print("Couldn't hide invalid input!")
# if row == 3:
#     if column == 1:
#         row3[0] = 'x'
#     elif column == 2:
#         row3[1] = 'x'
#     elif column == 3:
#         row3[2] = 'x'
#     else:
#         print("Couldn't hide invalid input!")

# print(row1)
# print(row2)
# print(row3)

# Where hide the treasure:
# row1 = ['😀','😅','😂']
# row2 = ['😁','😉','🙂']
# row3 = ['😋','😊','😇']
# map = [row1,row2,row3]
# print(row1)
# print(row2)
# print(row3)
# position = (input("Where do you want to hide the treasure?\n"))
# row = int(position[0])
# column = int(position[1])
# selectedR = map[row-1]
# selectedR[column-1] = 'X'

# print(row1)
# print(row2)
# print(row3)
    
# Where hide the treasure:
# row1 = ['😀','😅','😂']
# row2 = ['😁','😉','🙂']
# row3 = ['😋','😊','😇']
# map = [row1,row2,row3]
# print(row1)
# print(row2)
# print(row3)
# position = (input("Where do you want to hide the treasure? 'column then row':\n"))
# row = int(position[0])
# column = int(position[1])
# map[column-1][row-1] = 'X'#remember it looks like an array:
# #so now you can make some list and make a nested list it will work as an array
# print(row1)
# print(row2)
# print(row3)


# Day 4 final project:- Rock paper Scissors:
# import random
# rock =("""
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """)
# paper = ("""
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """)
# scissors =("""
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """)
# game = [rock, paper, scissors]
# choose = input("Do you want to play Rock paper scissors? 'Y' or 'N'\n")
# if choose == 'Y':
#     choose1 = int(input("Type 1 - rock, 2 - paper ,3 - scissors\n"))
#     if choose1 >= 4:
#         print("Invalid Input!! Exited.....")
#     else:
#         user_choice = game[choose1-1]
#         print("You chose:-\n",user_choice)
#         computer_index =  random.randint(0,(len(game)-1))
#         computer_choice = game[computer_index]
#         print("Computer Chose:-\n",computer_choice)
#         if user_choice == computer_choice:
#             print("Draw!")
#         elif user_choice == rock and computer_choice == paper:
#             print("You lost !")
#         elif user_choice == paper and computer_choice == scissors:
#             print("You lost!")
#         elif user_choice == scissors and computer_choice == rock:
#             print("You lost!")
#         else:
#             print("You won!")
# elif choose == 'N':
#     print("Thanks for using !!")
# else:
#     print("Invalid Input!! Exited.....")