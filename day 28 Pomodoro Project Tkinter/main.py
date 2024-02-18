import tkinter as t
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_stop = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer_stop)
    canvas.itemconfig(timer_text , text="00:00")
    timer.config(text="Timer" , font=(FONT_NAME, 35 , "underline") , fg= GREEN , bg=YELLOW )
    check_mark.config(text="")
    global reps 
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60 
    short_break_sec = SHORT_BREAK_MIN * 60 
    long_break_sec = LONG_BREAK_MIN * 60 

    if reps % 8 == 0:   
        count_down(long_break_sec)
        timer.config(text="Break" , font=(FONT_NAME, 35 , "underline") , fg= RED , bg=YELLOW )
    elif reps %2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break" , font=(FONT_NAME, 35 , "underline") , fg= PINK , bg=YELLOW )
    else:
        count_down(work_sec)
        timer.config(text="Work" , font=(FONT_NAME, 35 , "underline") , fg= GREEN , bg=YELLOW )
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


        
def count_down(count):
    #we don't want to round off the number just want to clear the decimals 
    global timer_stop
    count_min = math.floor(count/60)
    count_sec = math.floor(count%60)
    if count_sec <10:
        count_sec = f"0{count_sec}"
    #for changing text in canvas because its different than label 
    canvas.itemconfig(timer_text , text=f"{count_min}:{count_sec}")
    if count > 0:
        #adding delay to the command:
#USING THE AFTER METHOD(): it is a method which execute the commands after some delay
# args are 1. amount of time 2.function name
 
# def say_something(thing):
#     print(thing)

# #it actually passes positional arguments to the given function after the delay of 1000ms which is provided 
# window.after(1000, say_something , "hello")
        timer_stop = window.after(1000, count_down , count-1)
    else:
        start_timer()
        mark_check()


def mark_check():
    mark = ""
    work_sessions= math.floor(reps/2)
    for _ in range(work_sessions):
        mark += "✔"
    check_mark.config(text=mark , fg=GREEN , bg=YELLOW , highlightthickness=0)
    check_mark.grid(row=2, column=1)
        




# ---------------------------- UI SETUP ------------------------------- #
window = t.Tk()
window.title("The pomodoro Timer")
window.config(padx= 100 , pady= 50 , bg=YELLOW)



# Adding canvas to add image:
canvas = t.Canvas(height= 224 , width= 200 , bg=YELLOW , highlightthickness= 0)
#this is a predefined method to insert image path in the file
tomato_img = t.PhotoImage(file="day 28 Pomodoro Project Tkinter/tomato.png")
#canvas method to create an image:
canvas.create_image(100, 112, image=tomato_img )
#creating text in canvas and placing it on center
timer_text = canvas.create_text(100,130, text="00:00", font=(FONT_NAME , 35 , "bold" ), fill="white")

canvas.grid(row=1 , column= 1)


# Timer Label:
timer = t.Label()
timer.config(text="Timer" , font=(FONT_NAME, 35 , "underline") , fg= GREEN , bg=YELLOW )
timer.grid(row=0 , column= 1)



#Start button:
start = t.Button()
start.config(text="Start", font=(FONT_NAME,10,"normal"), highlightthickness= 0 ,command=start_timer)
start.grid(row=2 , column=0)



#Reset button:
reset = t.Button()
reset.config(text="Reset", font=(FONT_NAME,10,"normal") , highlightthickness= 0, command=reset_timer)
reset.grid(row=2 , column=4)


#check mark :
check_mark = t.Label()
 

window.mainloop()








window.mainloop()