import random
#Day 2:
# print("Calculating no. of days, months , years and weeks left if you live until 90:")
# age = float(input("Enter your age: "))
# numYears = 90 - age
# numMonths = int(numYears * 12)
# numWeeks = int(numYears * 52)
# numDays = int(numYears * 365)

# print(f"\nYou have {numYears} years , {numMonths} months, {numWeeks} weeks , {numDays} days left if you live until 90.")


#Day 3:
# print("Welcome to RollerCoaster: ")
# height = float(input("Enter your height: "))
# if height > 91.44:
#     age = int(input("Enter your age: "))
#     if age >=13:
#         print("You can ride")
#     elif age>=18:
#         print("You can ride without helmet")
#     else: 
#         print("You can not ride")
# else: 
#     print("Your height is not approved")

#Exercise: 
# print("Welcome to Body Mass Index Calculator:")
# height = float(input("Enter your height in meters: "))
# weight = float(input("Enter you weight in kgs: "))

# BMI = weight / (height**2)

# if BMI < 18.5:
#     print("You are underweight!")
# elif BMI >= 18.5 and BMI <25: 
#     print("You are normal weighted!")
# elif BMI >= 25 and BMI < 30:
#     print("You are overWeight!")
# elif BMI >= 30 and BMI <35: 
#     print("You are obese!")
# elif BMI > 35: 
#     print("You are clinically overweight!")
# else:
#     print("You are horribly Overweight and you need to see doctor soon!")

# print("Thank you for using!")

#Exercise: Leap Year

# print("Welcome to Leap Year Calculator: ")
# year = int(input("Enter the year: "))
# if year % 4 == 0:
#     if(year % 100 == 0):
#         if(year % 400 == 0):
#             print("Yes! it is a leap year")
#         else: 
#             print("Not a leap year")
#     else:
#         print("It is a leap year!")
# else: 
#     print("Not a leap Year!")

#Exercise: Love Calculator;

# print("Welcome to Love Calculator:")
# name1 = str(input("Enter first name: "))
# name2 = str(input("Enter second name: "))
# name = name1 + name2
# name.lower()
# t = name.count('t')
# r = name.count('r')
# u = name.count('u')
# e = name.count('e')
# l = name.count('l')
# o = name.count('o')
# v = name.count('v')
# e = name.count('e')

# sumLove = str(l+o+v+e)
# sumTrue = str(t+r+u+e)

# score = int(sumTrue +sumLove)
# print(f"Your score is {score} % ")
# if int(score) <=10 or int(score)>90:
#     print(f"you are like a coke and mentos together!")
# elif int(score)>20 and int(score)<50:
#     print("you are alright together!")


#Day 4:

#Banker Roulette's Exercise:

# print("Welcome to who will pay Roulette:")
# name = str(input("Give everyone's name seperated by ', ' : "))
# names = name.split(", ")
# chosen = random.randint(0,len(names)-1)
# print(f"{names[chosen]} is lucky to pay for everyone's bill")

# Exercise Rock Paper Scissors:

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
# computer_choice = random.choice(game)
# print("Do you want to play rock, paper, scissor? Type Y or N")
# ans = (str(input("Your choice:"))).lower()
# if ans == 'y':
#     print("Choose : 0 for rock , 1 for paper, 2 for scissors")
#     choose = int(input("Your choice: "))
#     user_choice = game[choose]
#     print("Your choice: ",user_choice)
#     print("Computer choice: ",computer_choice)
#     if user_choice == computer_choice:
#         print("Draw!")
#     elif user_choice == rock and computer_choice == paper:
#         print("You lost !")
#     elif user_choice == paper and computer_choice == scissors:
#         print("You lost!")
#     elif user_choice == scissors and computer_choice == rock:
#         print("You lost!")
#     else:
#         print("You won!")
# else: 
#     print("Thanks For using!")


#Exercise Hidden Treasure:


# row1 = ['😀','😅','😂']
# row2 = ['😁','😉','🙂']
# row3 = ['😋','😊','😇']

# map = [row1, row2, row3]
# print(row1)
# print(row2)
# print(row3)
# row = int(input("Where do you want to hide the treasure: \nRow: Type 1,2,3: \n"))
# column = int(input("Column: "))
# if row == 1: 
#     if column == 1:
#         map[0][0] = 'x'
#     elif column == 2:
#         map[0][1] = 'x'
#     elif column == 3:
#         map[0][2] = 'x'
#     else: 
#         print("Invalid Input!")
# elif row == 2:
#     if column == 1:
#         row2[0] = 'x'
#     elif column == 2:
#         row2[1] = 'x'
#     elif column == 3:
#         row2[2] = 'x'
#     else: 
#         print("Invalid Input!")
# elif row == 3:
#     if column == 1:
#         row3[0] = 'x'
#     elif column == 2:
#         row3[1] = 'x'
#     elif column == 3:
#         row3[2] = 'x'
#     else: 
#         print("Invalid Input!")

# print(row1)
# print(row2)
# print(row3)
    

#Day 5: 
#Exercise: Average Height

# Student_heights = (input("Enter the list of heights of students: ")).split()
# num_Students = 0
# Sum = 0
# for n in range(0,len(Student_heights)):
#     num_Students += 1
#     Sum += int(Student_heights[n])

# Average = Sum/len(Student_heights)

# print(f"The average height of {num_Students} students is {Average}")


#Exercise High score finder: 

# High_scores = input("Enter the list of student scores: ").split()
# highest = 0
# for score in High_scores: 
#     if int(score) >= highest:
#         highest = int(score)
# print(f"The highest score is : {highest}")


#Exercise Fizz :
# print("Welcome to Fizz:")
# for n in range(1, 101):
#     if n%3 == 0:
#         print("Fizz")
#     else: 
#         print(n)
# print("thanks")

# print("Welcome to Fizz - buzz :")
# for n in range(1,101):
#     if n%3 == 0 and n%5 == 0: 
#         print("Fizz-Buzz")
#     elAif n%5 == 0: 
#         print("Buzz")
#     elif n%3 == 0: 
#         print("Fizz")
#     else:
#         print(n)
# print("Thanks for using!")

#Exercise Random Password generator:
# letters = int(input("Enter the number of letters in your password: "))
# numbers = int(input("Enter the number of numberics you want: "))
# symbols = int(input("Enter the number of symbols you want: "))

# lettersList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbersList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# password = []
# symbolsList = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# for letter in range(0, letters):
#     l = lettersList[letter]
#     password += l
# for num in range(0,numbers):
#     n = numbersList[num]
#     password += n
# for sym in range(0,symbols):
#     s = symbolsList[sym]
#     password += s
# random.shuffle(password)
# Psswrd = ""
# for lis in password: 
#     Psswrd += lis

# print(Psswrd)

#Day 7 Recap: 
# logo = '''                                                                   
#  _ _ _  _____  __     _____  _____  _____  _____    _____  _____   
# | | | ||   __||  |   |     ||     ||     ||   __|  |_   _||     |  
# | | | ||   __||  |__ |   --||  |  || | | ||   __|    | |  |  |  |  
# |_____||_____||_____||_____||_____||_|_|_||_____|    |_|  |_____|  
#                                                                      _  | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/  
#                     ___________.._______
# | .__________))______|
# | | / /      ||
# | |/ /       ||
# | | /        ||.-''.
# | |/         |/  _  |
# | |          ||  `/,|
# | |          (\\`_.'
# | |         .-`--'.
# | |        /Y . . Y/
# | |       // |   | \/
# | |      //  | O |  \/
# | |     ')   |   |   (`
# | |          ||l||
# | |          || ||
# | |          || ||
# | |          || ||
# | |         / | | |
# """"""""""|_`-' `-' |"""|
# |"|"""""""\ \       '"|"|
# | |        \ \        | |
# : :         \ \       : :  
# . .          `'       . . '''
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''',
#  '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''',  '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''','''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
#     =========''']
# def hangman():
#     word_list = ["Aryan" , "Chhavi", "Vanshika"]
#     chosen_word = (random.choice(word_list)).lower()    
#     guess_list = []
#     end_of_game = False
#     num_lives = 6
#     for n in range(len(chosen_word)):
#         guess_list += "_"
#     print(guess_list)
#     while not end_of_game:
#         guess = (str(input("Guess a letter: "))).lower()
#         if guess in guess_list:
#             print("you've already guessed it!")
        
        
#         for n in range(len(chosen_word)):
#             if guess == chosen_word[n]:
#                 guess_list[n] = guess
#         if guess not in chosen_word:
#             num_lives -= 1
#             print(f"You chose wrong word.\nSo u lost a life: {num_lives} left.")
#             if num_lives == 0:
#                 print("You lose!")
#                 end_of_game = True

#         print(stages[num_lives])      
#         print(guess_list)

#         if "_" not in guess_list:
#             end_of_game = True
#             print(f"You won! with {num_lives} lives left.")
    

# print(logo)
# name = str(input("Enter your name: "))
# age = int(input("Enter your age: "))
# ask = (str(input("Do you want to play hangman? Type y, Y or n, N\n"))).lower()

# while ask != 'n':
#     if ask == 'y':
#         hangman()
#     elif ask != 'n':
#         print("Invalid input. Please enter 'y' or 'n'.")
    
#     ask = (str(input("Do you want to play again? Type y, Y or n, N\n"))).lower()

# print("Thanks for playing!")


#Day 8: Recap:

# def greet():
#     name = str(input("Enter your name: "))
#     print("Hello, Good morning " + name)
#     print("How are You?")
#     ans = str(input())

# greet()


# def greet_with_name(name):
#     print("Hello, Good morning " + name)
#     print("How are Ya?")
#     ans = str(input())
#     print("Good to hear!")

# greet_with_name("Aryan")

# Multiple arguments:
# def greet_with_name(name , address):
#     print("Hello, Good morning " + name)
#     print("How are Ya?")
#     ans = str(input())
#     print("oh okay")
#     print(f"How's the weather in {address}")
#     ans = str(input())
#     print("Good to hear!")

# greet_with_name("Gwalior" ,"Aryan")

# # Keywords arguments: doesn't follow order
# def greet_with_name(name , address):
#     print("Hello, Good morning " + name)
#     print("How are Ya?")
#     ans = str(input())
#     print("oh okay")
#     print(f"How's the weather in {address}")
#     ans = str(input())
#     print("Good to hear!")

# greet_with_name(address = "Gwalior" , name = "Aryan")

#Exercise 1:

# def Area_calc(length, breadth,coverage):
#     area = int(length) * int(breadth)
#     no_of_cans = round(area / coverage)

#     print(f"You will need {no_of_cans} cans to paint the wall.")



# print("Welcome to Paint area calculator! ")
# ask = str(input("Do you want to calculate paint area: "))
# if ask == 'y':
#     coverage = 5
#     height = float(input("Enter the height of wall: "))
#     width = float(input("Enter the width of wall: "))
#     Area_calc(height , width, coverage)
# else: 
#     print("Thanks for using!")


#exercise 2: Prime Checker!

# def prime_checker(n):
#     is_prime = True
#     for num in range(2,n-1):
#         if n % num == 0:
#             is_prime = False
        
#     if is_prime:
#         print("Prime.")
#     else: 
#         print("Not a prime.")
        


# print("Welcome to prime checker!")
# ask = (str(input("Do you want to check a number: Y or N\n"))).lower()
# if ask == 'y':
#     num = int(input("Enter the number: "))
#     prime_checker(num)
# else:
#     print("Thanks for using!")


    #Program: Caesar Cipher: 
# def caesar_cipher():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#     choose = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n")
#     msg = input("Enter your message: \n").lower()
#     shift = int(input("Enter the shift number: \n"))
#     def encrypt(msg,shift): 
#         cipher_text = ""
#         for letter in msg:
#             pos = letters.index(letter) #to get the index of particular letter from list of alphabets....
#             new_pos = pos + shift
#             new_pos %= 26
#             # using modulo to keep the index in range:

#             cipher_text += letters[new_pos]
                
#         print(f"The encrypted text is {cipher_text}")

#     def decrypt(cipher_text,shift):
#         global msg
#         msg = ""
#         for letter in cipher_text:
#             pos = letters.index(letter)
#             new_pos = pos - shift
#             msg += letters[new_pos]
#         print(f"The decoded text is {msg}")

#     if choose == "encode":
#         encrypt(msg,shift)
#     elif choose == "decode":
#         decrypt(msg,shift)
#     else: 
#         print("Invalid input!")
            
        

# ask = (str(input("Do you want to play Caesar Cipher? Type y, Y or n, N\n"))).lower()

# while ask != 'n':
#     if ask == 'y':
#         caesar_cipher()
#     elif ask != 'n':
#         print("Invalid input. Please enter 'y' or 'n'.")
    
#     ask = (str(input("Do you want to play again? Type y, Y or n, N\n"))).lower()

# print("Thanks for playing!")


# def caesar_cipher(msg, shift,direction):
#         letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#         cipher_text = ""
#         if direction == "decode":
#             shift *= -1
        
#         for letter in msg:
#             if letter in letters: #to leave spaces and symbols as it is...
#                 pos = letters.index(letter) #to get the index of particular letter from list of alphabets....
#                 new_pos = pos + shift
#                 new_pos %= 26
#                 # using modulo to keep the index in range:
#                 cipher_text += letters[new_pos]
#             else:
#                 cipher_text += letter
#         print(f"The {direction}d text is {cipher_text}.")
        

# ask = (str(input("Do you want to play Caesar Cipher? Type y, Y or n, N\n"))).lower()

# while ask != 'n':
#     if ask == 'y':
#         choose = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n")
#         if choose == 'encode' or choose == 'decode':
#             msg = input("Enter your message: \n").lower()
#             shift = int(input("Enter the shift number: \n"))
#             caesar_cipher(msg,shift,choose)
#         else:
#             print("Invalid input!")
#             break
#     elif ask != 'n':
#         print("Invalid input. Please enter 'y' or 'n'.")
    
#     ask = (str(input("Do you want to play again? Type y, Y or n, N\n"))).lower()

# print("Thanks for using!")


#day 9: Recap:

Student_scores = {
    "Aryan" : 9.5,
    "Chhavi" : 9.1,
    "Aditya" : 9.1,
    "Gourav" : 9.2,
    "Vanshika" : 8.5,
    "Ayush" : 7.6,
    "Arun" : 5.4
}
Student_grades = {}

for student in Student_scores:
    score = Student_scores[student]
    if score >= 9.0:
        Student_grades[student] = 'A'
    elif score >= 8.0 and score <9.0:
        Student_grades[student] = 'B'
    elif score >= 7.0 and score < 8.0:
        Student_grades[student] = 'C'
    elif score >=3.5 and score < 7.0:
        Student_grades[student] = 'D'
    else:
        Student_grades[student] = "F"

print(Student_grades)
        