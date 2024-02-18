# def greet():
#     print("Hello")
#     print("How are you?")
#     print("Where do you live?")

# greet()

# def greet_with_inputs(name,place):
#     print(f"Hello {name}")
#     print(f"How are you {name}?")
#     print(f"How is it in {place}?")

# greet_with_inputs("Aryan","Gwalior")

# def greet_with(name,place,age):
#     print(f"Hello {name}")
#     print(f"How are you {name}?")
#     print(f"How is it in {place}?")
#     print(f"You are {age} years old so you will be {age+2}years old after 2 years {name}")

# greet_with(place = "Dabra",name = "Vanshika",age = 18)
# import math 
# #math.ceil function is used to round the number by adding 1 (like 1.2 => 2) because paint can't be less so we need to use this instead of round() function...
# def paint_calc(height,width,cover_5):
#     area_wall = height*width
#     no_of_cans = math.ceil(area_wall/cover_5)
#     print(f"You will need {no_of_cans} can/cans to paint this wall")

# height = float(input("Enter the height of the wall:-(in meters)  "))
# width = float(input("Enter the width of the wall:-(in meters)  "))
# cover_5 = 5

# paint_calc(height,width,cover_5)

# n = int(input("Check this number:- "))

# def prime_checker(number):
#     is_prime = True
#     for num in range(2,n):
#         if n%num == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number")
#     else:
#         print("It's not a prime number")


# prime_checker(n)
# alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
# text = str(input("Enter the code:\n")).lower()

# n = int(input("Enter the shift number:-\n"))
# def encrypt(plain_text,shift):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabets.index(letter)
#         new_position = position + shift
#         cipher_text += alphabets[new_position]
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text,shift):
#     decode = ""
#     for letter in cipher_text:
#         position = alphabets.index(letter)
#         new_position = position - shift
#         decode += alphabets[new_position]
#     print(f"The decoded text is {decode}")

# if direction == 'decode':
#     decrypt(text,n)
# elif direction == 'encode':
#     encrypt(text,n)
# else:
#     print("Invalid input!! Exited....")


# alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
# text = str(input("Enter the code:\n")).lower()

# shift = int(input("Enter the shift number:-\n"))
# def caesar_cipher(input_code,shift_amount,directions):
#     output_code = ""
#     if direction == "decode":
#         shift_amount *= -1
#     for letter in input_code:
#         position = alphabets.index(letter)
#         new_position = position + shift_amount
#         output_code += alphabets[new_position]
#     print(f"The {direction}d text is {output_code}")

# caesar_cipher(input_code = text, shift_amount = shift , directions = direction)


# shifted = shift % 26
# keep_running = True
# while keep_running == True:
#     alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
#     text = str(input("Enter the message:\n")).lower()
#     shift = int(input("Enter the shift number:-\n"))
#     def caesar_cipher(input_code,shift_amount,directions):
#         output_code = ""
#         if direction == "decode":
#             shift_amount *= -1
#         for char in input_code:
#             if char in alphabets :
#                         position = alphabets.index(char)
#                         new_position = position + shift_amount
#                         new_position = new_position % 26
#                         output_code += alphabets[new_position]
#             else:
#                 output_code += char       

#         print(f"The {direction}d text is {output_code}")


#     caesar_cipher(input_code = text, shift_amount = shift, directions = direction)
#     ask = str(input("Do you want to go again? type 'yes' or 'no'\n")).lower()
#     if ask == 'no':
#         keep_running = False
#         print("Thanks for using!!")
#     elif ask == 'yes':
#         keep_running = True
#     else:
#         keep_running = False
#         print("Invalid Input!")

travel_log = {
    "Madhya_pradesh":{"Cities_visited":[
            "Gwalior":8,
            "Bhopal":1,
            "Indore":5,
            "Seoni": 1
            ]}
    "Rajasthan": {
        "Cities_visited":[
            "Kota": 2,
            "Jaipur": 4,
        ]
    }
}
print(travel_log)











