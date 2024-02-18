import tkinter as t
import json
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
new_card = {}
to_learn = {}

try:
    data = pandas.read_csv("day31 Flashcard Capstone project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("day31 Flashcard Capstone project/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
#------------------------------Saving words not in new card----------------------------#
def is_known():
    to_learn.remove(new_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("day31 Flashcard Capstone project/data/words_to_learn.csv", index=False)
    new_word()

# -------------------Flashing the back of the card------------------#
def Flash_card():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(title , text = "English" , fill="white")
    canvas.itemconfig(word , text =new_card["English"], fill="white")



#-------------------------DISPLAY NEW WORD ON CLICK BUTTON------------------------#

    


def new_word():

    global new_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(title ,text="French" , fill ="black")
    new_card = random.choice(to_learn)
    canvas.itemconfig(word ,text=new_card["French"], fill ="black" )
    canvas.itemconfig(card_img , image = card_front_img)
    flip_timer = window.after(3000 , func=Flash_card )

    

# ----------------------------UI SETUP----------------------------#
window = t.Tk()
window.title("The Flashcard Program")
window.config(padx=50 , pady=50 , bg=BACKGROUND_COLOR)
flip_timer = window.after(3000 , func=Flash_card )

# creating canvas
canvas = t.Canvas()
canvas.config(width=800 , height=526 , bg=BACKGROUND_COLOR ,highlightthickness=0 )
card_front_img = t.PhotoImage(file="day31 Flashcard Capstone project/images/card_front.png")
card_back_img = t.PhotoImage(file="day31 Flashcard Capstone project/images/card_back.png")
card_img = canvas.create_image(400,258,image = card_front_img )
title = canvas.create_text(400 , 150 , text="Title" , font=("Arial" , 40 , "italic"))
word = canvas.create_text(400, 258 , text="Word" , font=("Arial", 50 , "bold"))

canvas.grid(row=0 , column=0,columnspan=2)

#setting buttons to change flash cards:
check_image = t.PhotoImage(file="day31 Flashcard Capstone project/images/right.png")
check_btn = t.Button(image=check_image,highlightthickness=0 )
check_btn.config(command= is_known)
check_btn.grid(row=1 , column=1)

cross_img = t.PhotoImage(file="day31 Flashcard Capstone project/images/wrong.png")
cross_btn = t.Button(image=cross_img ,highlightthickness=0 )
cross_btn.config(command=is_known)
cross_btn.grid(row=1 , column=0)

new_word()


window.mainloop()




