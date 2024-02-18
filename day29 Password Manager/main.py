import tkinter as t
from tkinter import messagebox
import random
import pyperclip
import json
#----------------------------Search Data--------------------------#
def search_data():
    webiste_entered = website_text.get()
    try:
        with open("day29 Password Manager/data.json",mode='r') as data_file:
            data = json.load(data_file)
        messagebox.showinfo(title=f"{webiste_entered.title()}",message=f"Email: {data[webiste_entered]['email']}\nPassword: {data[webiste_entered]['password']} ")
    except KeyError:
        messagebox.showerror(title="Key Error!", message="Oops! Data not found.")
    except FileNotFoundError as f:
        messagebox.showerror(title=f"{f}" , message="File does not exist!")
    else:
        website_text.clear(0,t.END)
        password_txt.clear(0,t.END)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    Password = []
    no_of_letters = random.randint(8,10)
    no_of_symbols = random.randint(2,4)
    no_of_numbers = random.randint(2,4)

    password = [random.choice(letters) for char in range(no_of_letters)]
    symbol = [random.choice(symbols) for char in range(no_of_symbols)]
    number = [random.choice(numbers) for char in range(no_of_numbers)]

    Password = password + symbol + number
    random.shuffle(Password) 
    # str_password = ""
    # for lis in Password:
    #     str_password += lis

    # python JOIN METHOD TO CREATE STRING OUT OF LIST, TUPLE OR DICTIONARY:
    str_password = "".join(Password)
    
    password_txt.delete(0,t.END)
    password_txt.insert(0,str_password)
    pyperclip.copy(str_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_entered = website_text.get()

    username_entered = username_txt.get()
    pass_entered = password_txt.get()
    entry = {
         website_entered: {
              "email": username_entered
              ,"password" : pass_entered
         }
    }
    if len(pass_entered) == 0 or len(website_entered) == 0:
        messagebox.showerror(title="Oops!" , message="You have left some fields empty! Can't save details")
    else:
        try:
            with open("day29 Password Manager/data.json", 'r') as data_file:
                data = json.load(data_file)
                  #saving the data in the file:
        except FileNotFoundError:
            with open("day29 Password Manager/data.json" , 'w') as data_file:
                json.dump(entry,data_file, indent=4)
        else:
            #updating the data to new_data:
            data.update(entry)
            with open("day29 Password Manager/data.json" , 'w') as data_file:
                json.dump(data,data_file, indent=4)
        password_txt.delete(0, t.END)
        website_text.delete(0, t.END)
        
    

    
# ---------------------------- UI SETUP ------------------------------- #
window = t.Tk()
window.title("The Password Manager")
window.config(padx = 50 , pady = 50)


#creating Canvas
canvas = t.Canvas()
canvas.config(width=200 , height= 200)
logo = t.PhotoImage(file ="day29 Password Manager/logo.png")
canvas.create_image(100, 100 ,image = logo)
canvas.grid(row=0, column=1)

#Creating the labels:

#Website label:
website = t.Label()
website.config(text="Website:")
website.grid(row=1, column=0)

#Email/usernamer label

username = t.Label()
username.config(text="Email/Username:")

username.grid(row=2, column=0)


# Passwords label

password = t.Label()
password.config(text="Password:")
password.grid(row=3, column=0 )



#text Areas for all :
website_text = t.Entry()
website_text.focus()
website_text.config(width=21)
website_text.grid(row=1, column=1,columnspan=2 ,padx=22, sticky='w')

#username text area:
username_txt = t.Entry()
username_txt.config(width=35)
username_txt.insert(0, "aaryangupta636@gmail.com")
username_txt.grid(row=2, column=1, columnspan=2)


#password text area:
password_txt = t.Entry(width=15)
password_txt.grid(row=3, column=1 , sticky="w" , padx=24)

#Generate Password Button:
generate_btn = t.Button()
generate_btn.config(text="Generate Password" , command=password_generator)
generate_btn.grid(column=1, row=3 ,sticky="e")

#Add Password button:
add_btn = t.Button()
add_btn.config(text="Add" , width=36 , command=save_password)
add_btn.grid(row=4 , column=1 , columnspan=2)

#Search Button:
search_btn = t.Button()
search_btn.config(text="Search" , width=10 ,command=search_data)
search_btn.grid(row=1 , column=1 , columnspan=2 , sticky='e' , padx=24)

    

window.mainloop()
