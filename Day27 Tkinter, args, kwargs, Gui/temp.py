#unlimited positional arguments:
#Their type is 'tuple' 
# def add(*nums):
#     sum = 0
#     for num in nums:
#         sum += num 
#     return sum

# print(add(2,3,4,5,6))

#kwargs aka keyworded arguments:
#The type of these args is "Dictionary"

# def calculate(n,**kwargs):
#     n += kwargs['add']
#     n *= kwargs['multiply'] 

#     print(n)

# calculate(2,add = 3 , multiply = 5)

# class Car: 
#     def __init__(self,**kw):
#         self.make = kw["make"]
#         self.model = kw["model"]

# my_car = Car(make = "Lamborghini" , model = "gt")
# print(my_car.model)

#THERE'S A PROBLEM: IT CRASHES IF KEY IS NOT PRESENT SO WE USE ANOTHER METHOD:::::
class Car: 
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make = "Lamborghini")
print(my_car.model) #It will show none:


