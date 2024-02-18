import tkinter as t

window = t.Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500 ,height=500)

#label

my_label = t.Label(text="Miles", font=("ARial", 20, "bold"))

#we can change the text and other properties of label "one by one "or of "whole"

my_label["text"] = "New Text"
my_label.grid(row=0, column=0)

#by using config() METHOD:
my_label.config(text="Nacho mere sath ")

def button_clicked():
    my_label["text"] = "Button clicked"
    var = input.get()
    print(var)

button = t.Button(text="Click Me!", command=button_clicked)
button.grid(row=1,column=1)


button2 = t.Button(text="Click Me 2!")
button2.grid(row=0 , column=2)

#Entry:
input = t.Entry()
input.grid(row=3 , column=3)










window.mainloop()