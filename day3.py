# Day :- 3
# print("Welcome to Even or odd number checker:-")
# n = int(input("Enter any number:-"))
# if n%2 == 0:
#     print(f"{n} is an even number:")
# else:
#     print(f"{n} is an odd number:")

# print("Welcome to RollerCoaster!")
# height = int(input("What's your height in cm?\n"))
# if height>=120:
#     print("You are tall enough to ride.")
#     age = int(input("Now, Enter your age:-"))
#     if age>=18:
#         print("You just need to pay 60rs for the ride:)")
#     else:
#         print("You need to pay 40rs for the ride:)")
# else:
#     print("Sorry! You are not tall enought to enjoy the ride:")

# print("Thanks for coming!!")

# print("Welcome to Body mass Index calculator:-")
# Weight = float(input("Enter your weight in Kgs:-"))
# height = float(input("Enter your height in m:-"))
# BMI = (Weight/(height**2))
# print("Your Body mass Index is ",round(BMI,2),"kg/m^2")
# if BMI<18.5:
#     print("You are underweight.\nYou need to take a healthy diet")
# elif BMI>=18.5 and BMI<25:
#     print("You are Normal.Congo!")
# elif BMI>=25 and BMI<30:
#     print("You are overweight.\nYou need to loose weight")
# elif BMI>=30 and BMI<35:
#     print("You are obese.\nYou need to follow a strict diet and loose weight")
# else:
#     print("You are clinically obese.\nYou need to see a doctor ASAP.")

# print("Thank You!!")

# Project :- Leap year
# print("Welcome to the Leap Year Detector:-")
# year = int(input("Enter the year you want to check as a leap year:"))
# if year%4 == 0:
#     if year%100 ==0:
#         if year%400 == 0:
#             print(f"The year {year} is a leap year:")
#         else:
#             print(f"The year {year} is not a leap year")
#     else:
#         print(f"The year {year} is a leap year")
# else:
#     print(f"The year {year} is not a leap year")

# print("Welcome to RollerCoaster!")
# height = int(input("What's your height in cm?\n"))
# if height>=120:
#     print("You are tall enough to ride.")
#     bill = 0
#     age = int(input("Now, Enter your age:-"))
#     if age>=18:
#         print("You just need to pay 60rs for the ride:)")
#         bill = 60
#     elif age<18 and age>=12:
#         print("You need to pay 40rs for the ride:)")
#         bill = 40
#     else:
#         print("You just need to pay 20rs for the ride")
#         bill = 20
#     photo = input("Do you want to get a photo taken?\nType 'Y' for yes or 'N' for No:- ")
#     if photo == 'Y':
#         bill += 30
#         print(f"Your Total bill is {bill}rs.")
#     else:
#         print(f"Your Total bill is {bill}rs.")

# else:
#     print("Sorry! You are not tall enought to enjoy the ride:")

# print("Thanks for coming!!\nHope you enjoyed the ride.")

# project :- Pizza order 
# print("Welcome to Python Pizza deliveries!")
# size = input("Choose the size of pizza you want? S, M or L\n")
# pepperoni = input("Do you want pepperoni? Y or N\n")
# cheese = input("Do you want extra cheese on the pizza? Y or N\n")
# if size == 'S':
#     bill = 150
#     if pepperoni == 'Y':
#         bill += 40
#     if cheese == 'Y':
#         bill += 50
#     print(f"Order Confirmed! Your Total bill is {bill}Rs.")
# elif size == 'M':
#     bill = 200
#     if pepperoni == 'Y':
#         bill += 80
#     if cheese == 'Y':
#         bill += 50
#     print(f"Order Confirmed! Your Total bill is {bill}Rs.") 
# elif size == 'L':
#     bill = 250
#     if pepperoni == 'Y':
#         bill += 80
#     if cheese == 'Y':
#         bill += 50
#     print(f"Order Confirmed! Your Total bill is {bill}Rs.") 
# else:
#     print("Invalid Input! Order Cancelled..")
# print("Thank You! for contacting Python Pizzas..")

# print("Welcome to RollerCoaster!")
# height = int(input("What's your height in cm?\n"))
# if height>=120:
#     print("You are tall enough to ride.")
#     bill = 0
#     age = int(input("\Please enter your age:-"))
#     if age>=18 and age<45:
#         bill = 60
#         print("\nYou just need to pay 60rs for the ride:)")
#     elif age<18 and age>=12:
#         bill = 40
#         print("\nYou need to pay 40rs for the ride:)")
#     elif age>=45 and age<= 55:
#         bill = 0
#         print("\nThe ride is free for this age group.Enjoy!!")
#     else:
#         bill = 20
#         print("\nYou just need to pay 20rs for the ride")
#     photo = input("\nDo you want to get a photo taken?\nType 'Y' for yes or 'N' for No:- ")
#     if photo == 'Y' and (age>=45 and age<=55):
#         bill == 0
#         print(f"\nYour total bill is {bill}rs.\nEnjoy your ride!!")
#     elif photo == 'Y':
#         bill += 30
#         print(f"\nYour Total bill is {bill}rs.")
#     else:
#         print(f"\nYour Total bill is {bill}rs.")
# else:
#     print("Sorry! You are not tall enought to enjoy the ride:")
# print("Thanks for coming!!\nHope you enjoyed the ride.")

print("Welcome to Love Calculator:")
name1 = str(input("What is your name?\n"))
name2 = str(input("What is their name?\n"))
name = name1+name2
name.lower()
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
sumlove = str(l+o+v+e)
sumtrue = str(t+r+u+e)
score = sumtrue+sumlove  
if  int(score) <=10 or int(score) >=90:
    print(f"your score is {score}%, you go together like coke and mentos.")
elif int(score)>40 and int(score)<50:
    print(f"your score is {score}%, you are alright together.")
else:
    print(f"Your love score is {score}%.")