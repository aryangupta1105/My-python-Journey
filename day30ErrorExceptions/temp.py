# try:
#     file = open("day30ErrorExceptions/my_file.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("day30ErrorExceptions/my_file.txt" , 'w')
#     file.write("File created")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File Closed!")


# EXERCISE 1:
# fruits = eval(input())


# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError :
#         print("Fruit pie")
#     else:
#         print(fruit + "pie")

# make_pie(4)

#Exercise 2:

facebook_posts = eval(input())

total_likes = 0
for post in facebook_posts:
    try:
        total_likes += post['Likes']
    except IndexError:
        total_likes += 0

print(total_likes)