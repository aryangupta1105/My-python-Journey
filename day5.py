# Day 5
# print("Welcome to even adder:")
# sum = 0
# for n in range(0,101,2):
#     # print(n)
#     sum += n
# print(f"Sum is {sum}")

# print('Welcome to Fizz Buzz exercise!')
# for number in range(1,101):
#     if number % 5== 0 and number %3 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0 :
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)
# print("Thank You!!")


import random 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

Password = []
no_of_letters = random.randint(8,10)
no_of_symbols = random.randint(2,4)
no_of_numbers = random.randint(2,4)


for password in range(0,no_of_letters):
    l = random.choice(letters)
    Password += l
# Password.split()
for password in range(0,no_of_symbols):
    s = random.choice(symbols)
    m = random.randint(0,len(Password)-1)
    Password[m] += s
for password in range(0,no_of_numbers):
    n = random.choice(numbers)
    m = random.randint(0,len(Password)-1)
    Password[m] += n
str_password = ''
for lis in Password:
    str_password += lis
print("Here is your Password:- ",str_password)