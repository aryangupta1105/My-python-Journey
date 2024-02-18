# #concepts i learned in this projects :
# #ALL NEW THINGS:
# def start_timer():
#     count_down(5*60)
# min = 5
# def count_down(count):
#     #we don't want to round off the number just want to clear the decimals 
#     count_min = math.floor(count/60)
#     count_sec = math.floor(count%60)
#     #for changing text in canvas because its different than label 
#     canvas.itemconfig(timer_text , text=f"{count_min}:{count_sec}")
#     if count > 0:
#         window.after(1000, count_down , count-1)

# #adding delay to the command:
# #USING THE AFTER METHOD(): it is a method which execute the commands after some delay
# # args are 1. amount of time 2.function name
 
# # def say_something(thing):
# #     print(thing)

# # #it actually passes positional arguments to the given function after the delay of 1000ms which is provided 
# # window.after(1000, say_something , "hello")



#dynamic typing in python:
#WE can change the datatype of the variable by changing its content
