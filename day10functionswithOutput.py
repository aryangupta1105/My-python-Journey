#Day 10: Functions with output:

# def format_name(fname , lname):
#     full_name = (fname + " " + lname).title()
#     return full_name


# name = (input("Enter a string: ").lower()).split()
# first = name[0]
# last = name[1]
# print(format_name(first , last))

#Exercsie Calculate no. of days of any month and year

# def check_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else: 
#                 return False
#         else: 
#             return True
#     else:
#         return False


# def num_days_month(year, month):
#     Days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 , 31]
#     if check_leap_year(year) == True and month == 2:
#         Days_in_month[1] = 29
#     else: 
#         Days_in_month[1] = 28

#     return Days_in_month[month-1]
   

# print("Welcome to days Counter:!")
# year = int(input("Enter the year: "))
# month = int(input("Enter the month number: (1 to 12)\n"))
# if not (month <= 12 and month >= 1 and year >= 1):
#     print("Invalid input!")
# else:
#     num_days = num_days_month(year,month)
#     print(f"The {year} has {num_days} days in the month number {month} .")


#Exercise: Final Calculator Project: 

def sum(num1, num2):
    output = num1 + num2
    print(f"{num1} + {num2} = {output}")
    return output

def mul(num1 , num2):
    output = num1 * num2
    print(f"{num1} * {num2} = {output}")
    return output
def div(num1 , num2):
    output = num1 / num2
    print(f"{num1} / {num2} = {output}")
    return output
def sub(num1 , num2):
    output = num1 - num2
    print(f"{num1} - {num2} = {output}")
    return output



def calculator():
    first_num = float(input("What's the first number: "))
    keep_running = True 
    while keep_running:
        chosen_operator = (input("Choose the operation: \n+\n-\n*\n/\n"))
        
        operators ={
        '+' : sum,
        '-' : sub,
        '*' : mul,
        '/' : div
    }  
        if chosen_operator in operators:
            operation = operators[chosen_operator]
        else:
            print("Invalid input!")
            break
        second_num = float(input("What's the second number: "))
        
        output = operation(first_num,second_num)
                #can also do by if-else ladder:
            # if choose == '+':
            #     output = sum(first_num,second_num)
            # elif choose == '-':
            #     output = sub(first_num,second_num)
            # elif choose == '*':
            #     output = mul(first_num,second_num)
            # elif choose == '/':
            #     output = div(first_num,second_num)
            # else: 
            #     print("Invalid input!")


        ask = input("Type 'y' to continue with same output.Or Type 'n' to start a new calculation Or 'exit' to end\n").lower()
        if ask == 'y':
            first_num = output
        elif ask == 'n':
            first_num = float(input("What's the first number: "))
        elif ask == 'exit':
            print(f"The final output is {output}")
            print("Thanks for using!")
            keep_running = False
        else:
            print("invalid input! Program Exited...")
            keep_running = False
    

calculator()

