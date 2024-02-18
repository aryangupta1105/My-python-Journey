import tkinter as t
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"

new_card = {}
to_learn = {}
#--------------------Choosing a random word--------------------#
try:
    data = pandas.read_csv("day31 Flashcard Capstone project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("day31 Flashcard Capstone project/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def is_known():
    to_learn.remove(new_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(file="day31 Flashcard Capstone project/data/words_to_learn.csv" , index=False)
    next_word()

def next_word():
    global new_card , flip_timer
    window.after_cancel(flip_timer)
    new_card = random.choice(to_learn)
    canvas.itemconfig(title,text="French" , fill = "black")
    canvas.itemconfig(card_image , image = card_front_img)
    canvas.itemconfig(word,text=new_card['French'], fill = "black")
    flip_timer = window.after(3000 , func=Flash_card )


#---------------------Flashing card--------------#
def Flash_card():
    canvas.itemconfig(card_image , image=card_back_img)
    canvas.itemconfig(title , text="English" , fill="white")
    canvas.itemconfig(word , text=new_card['English'] , fill="white")
    

    


#-------------------UI SETUP-----------------------#
window = t.Tk()
window.config(bg= BACKGROUND_COLOR ,padx=50 , pady= 50)
window.title("The french Flashcards")
flip_timer = window.after(3000 , func=Flash_card)



#------------------Canvas-------------------#
canvas = t.Canvas()
canvas.config(width=800 , height=526 ,bg=BACKGROUND_COLOR , highlightthickness= 0)
card_front_img = t.PhotoImage(file="day31 Flashcard Capstone project/images/card_front.png")
card_back_img = t.PhotoImage(file="day31 Flashcard Capstone project/images/card_back.png")
card_image = canvas.create_image(400 , 258 ,image = card_front_img)



# ----------------------Creating text labels ---------------#
#title
title = canvas.create_text(400 , 150 , text="Title",font=("Arial",40,"italic"), fill= "black")
#word
word = canvas.create_text(400 , 263 , text="word",font=("Arial",60,"bold"), fill= "black")


canvas.grid(row=0 , column=0 ,columnspan=2)


# ----------------------Creating buttons---------------------#
correct_img = t.PhotoImage(file="day31 Flashcard Capstone project/images/right.png")
correct_btn = t.Button(image=correct_img)
correct_btn.config(background=BACKGROUND_COLOR, highlightthickness=0 ,command=is_known)
correct_btn.grid(row=1 , column=1 )



wrong_img = t.PhotoImage(file="day31 Flashcard Capstone project/images/wrong.png")
wrong_btn = t.Button(image=wrong_img)
wrong_btn.config(background=BACKGROUND_COLOR, highlightthickness=0)
wrong_btn.grid(row=1 , column=0)





next_word()











window.mainloop()