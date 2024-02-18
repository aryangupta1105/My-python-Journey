# nums = [1,1,2,3,5,8,13,21,34,55]
# squared_nums = [num**2 for num in nums]
# print(squared_nums)

# list_of_strings = input().split(',')
#
# even_list = [num for num in list_of_strings if int(num)%2 == 0]
# print(even_list)

#Hard Exercise
# with open("day26 ListComprehension and NATO Alphabets/file1.txt" , mode='r') as file1:
#     data1 = file1.read().split('\n')
# with open("day26 ListComprehension and NATO Alphabets/file2.txt" , mode='r') as file2:
#     data2 = file2.read().split('\n')

# result = [int(data) for data in data1 if data in data2 ]
# print(result)


#UPDATE: IN US STATE GAME:
# missed_states = {
#             "Missed States" : 
#             [state for state in all_states if state not in guessed_states]
#         }


#DICTIONARY COMPREHENSION:

# syntax := new_dict = {new_key:new_value for item  in list}
# syntax 2 := new_dict = {new_key:new_value for (key,value)  in dict.items()}

# sentence = input()
# word_dic = {word:len(word) for word in sentence.split(" ")}
# print(word_dic)

# weather_c = eval(input())
#eval() takes input directly as dictionary
# print(weather_c)
# weather_f = {temp: in_c*9/5+32 for (temp, in_c) in weather_c.items()}
# print(weather_f)


#HOW TO ITERATE THROUGH DATAFRAMES IN PYTHON:

#looping through dictionaries:
student_dict ={
    "Student" : ["Aryan" , "Chhavi", "Ayushi"]
    ,"score" : [95,92,76]
}

# for (key,value) in student_dict.items():
#     print(key + ":")
#     print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#THIS METHOD IS NOT EFFECTIVE BASICALLY LOOPING:
# for (key,value) in student_data_frame.items():
#     print(value)


#PANDAS HAVE ITS OWN METHODS : ITTEROWS:

# for (index,row) in student_data_frame.iterrows():
#     # print(index)
#     if index == 1:
#         print(row)