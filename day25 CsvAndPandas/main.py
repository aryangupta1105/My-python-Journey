# with open("day25 CsvAndPandas/002 weather-data.csv" , mode='r') as weather_file:
#     days = weather_file.readlines()
# print(days) 

#inbuilt Library: 
# import csv
# with open("day25 CsvAndPandas/002 weather-data.csv" , mode='r') as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     # print(data) #It has created a object having all the data
#     #WE can now loop through the data and print each row or column
#     for row in data:
#         temperatures.append(row[1])
#     temperatures = temperatures[1:]
#     print(temperatures)

import pandas
# data = pandas.read_csv("day25 CsvAndPandas/002 weather-data.csv" )
# print(data["temp"])

# temp_list = data["temp"].to_list()

# average = sum(temp_list) /len(temp_list)
# print(round(average,2))

#predefined methods for statistical data
# 1: Mean()
# print(round(data["temp"].mean(),2))
# 2. Max()
# print(data["temp"].max())
#3. Min()
# print(data["temp"].min())
#4.Mode()
# print(data["temp"].mode())
#5. Median()
# print(data["temp"].median())


#To get hold of any row in data Table:

# print(data[data.day == "Monday"])


#challenge: to get the row with max temp:
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0] * 9/5 + 32
# print(f"Monday's temp in Farenheit:  {round(monday_temp,2)}'F")


#How to create data_frame from Scratch: 
# student_data = {
#     "Students" :["Aryan", "Chhavi", "Vanshika", "Manasvi", "Chetan", "Ayush"]
#     ,"Scores" : [9.5, 9.1, 8.5, 8.8, 8.7 ,8.7]

# }


# data = pandas.DataFrame(student_data)
# print(data)
# data.to_csv("Students_score.csv")

#example to get count of repeating things:
# temp_24_count = len(data[data.temp == 14])
# print(temp_24_count)


#Challenge
squirrel_data = pandas.read_csv("day25 CsvAndPandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240122.csv")
gray_squirrels =len( squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
Black_squirrels =len( squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

fur_color_count = {
    "Fur Color" : ["Gray" , "Cinnamon" , "Black"] ,
    "Squirrels Count" : [gray_squirrels,cinnamon_squirrels,Black_squirrels]
}

print(fur_color_count)

squirrel_data = pandas.DataFrame(fur_color_count)
squirrel_data.to_csv("fur_colour_count.csv")


