# student_scores = {
#     "Aryan" : 98,
#     "Vanshika": 90,
#     "Manasavi": 84,
#     "Sejal": 75,
#     "Yashi":63
# }
# student_grades = {}
# for scores in student_scores:
#     if student_scores[scores] < 70:
#         student_grades[scores] = "fail"
#     elif student_scores[scores] > 70 and student_scores[scores] < 81:
#         student_grades[scores] = "acceptable"
#     elif student_scores[scores] > 80 and student_scores[scores] < 91:
#         student_grades[scores] = "Exceeds expectations"
#     else:
#         student_grades[scores] = "Outstanding"

# print(student_grades)


# student_scores = {
#     "Aryan" : 98,
#     "Vanshika": 90,
#     "Manasavi": 84,
#     "Sejal": 75,
#     "Yashi":63
# }
# student_grades = {}
# for students in student_scores:
#     score = student_scores[students] 
#     if score < 70:
#         student_grades[students] = "fail"
#     elif score > 70 and score < 81:
#         student_grades[students] = "acceptable"
#     elif score > 80 and score < 91:
#         student_grades[students] = "Exceeds expectations"
#     else:
#         student_grades[students] = "Outstanding"

# print(student_grades)

# Nesting dictionaries and Lists:

# Student_marks = {
#     "Aryan" : {"Marks":{"Maths": 98 , "Dsa": 98 , "Coa": 92 , "Dc":89}} #Dictionary inside Dictionary inside Dictionary
#    , "Chhavi" : {"Maths": 94 , "Dsa": 95 , "coa": 93, "Dc": 94} #Dictionary inside Dictionary
# }
# print(Student_marks["Aryan"]["Marks"]["Maths"]) #just like a matrix...
# print(Student_marks["Chhavi"]["Maths"]) #just like a matrix...

# Student_marks = [
#     {
#         "name" : "Aryan",
#         "Total_Marks" : 279,
#         "Dsa_marks" : 98,
#         "Coa_marks" : 92,
#         "Dc_marks" : 89
#     }
#     ,
#     {
#         "name" : "Chhavi",
#         "Total_marks" : 280,
#         "Dsa_marks" : 95,
#         "Coa_marks" : 94,
#         "Dc_marks" : 91
#     }
# ]

# for details in Student_marks[0]:
#     print(details)
#     print(Student_marks[0][details])


#Country Log Exercise:

# country = str(input("Enter the country visited: "))
# no_of_visits = int(input("Enter the number of visits: "))
# list_of_cities =(str(input("Enter the list of cities: ")) ).split(" ")

# travel_log = [
#     {
#         "Country" : "India",
#         "Visits" : 156 ,
#         "Cities_visited" : ["Indore" , "Bhopal" , "Delhi" , "Banglore" , "Mumbai" , "Hyderabad" , "Chennai" , "Patna"]
#     },
#     {
#         "Country" : "UAE",
#         "Visits" : 12,
#         "Cities_visited" : ["Dubai" , "Abu Dhabi" , "Sharjan"]
#     },
# ]

# def travel_log_generator(country, visits, cities):
#     new_country = {}
#     new_country["Country"] = country
#     new_country["Visits"] = visits
#     new_country["Cities_visited"] = cities
#     travel_log.append(new_country)
#     n = len(travel_log) - 1
#     print(travel_log[n])
# travel_log_generator(country , no_of_visits , list_of_cities)

#Biding auction program: 

import os
keep_bidding = True
print("Welcome to Secret Auction Porgram.")


bidders_list = []
def bidding_taker(name , bid):
    new_bid = {}
    new_bid["name"] = name
    new_bid["biding_amount"] = bid
    bidders_list.append(new_bid)
    
def highest_bidder(bidder_list):
    winner = ""
    max_bid_amount = 0
    for n in range(len(bidder_list)):
        if bidder_list[n]["biding_amount"] > max_bid_amount:
            max_bid_amount = bidder_list[n]["biding_amount"]
            winner = bidder_list[n]["name"]
    print(f"{winner} has won the bid with a value of {max_bid_amount} dollars.")

while keep_bidding:
    bidders_name = str(input("Enter your name: "))
    biding_amount = int(input("What's your bid?\n"))
    bidding_taker(bidders_name,biding_amount)
    bidders = str(input("Are there any other bidders? Type 'yes' or 'no'\n")).lower()
    os.system('cls')
    # clear()
    if bidders == 'no':
        highest_bidder(bidders_list)
        keep_bidding = False
    elif bidders != 'yes':
        keep_bidding = False
        
    
        
