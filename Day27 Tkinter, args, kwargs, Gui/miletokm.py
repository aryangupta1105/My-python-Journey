import tkinter as t

window = t.Tk()
window.minsize(height=100 , width= 200)
window.title("Mile to km Converter")

window.config(padx=10 , pady= 20)
def convert():
    miles = float(input.get())
    km =  miles * 1.609
    output.config(text=km)


#text input:
input = t.Entry()
input.grid(row=0, column=1)
input.config(width=7)

#Miles Label
label1 = t.Label()
label1.config(text="Miles")
label1.grid(row=0 , column=2)


#Kilometer Label
label2 = t.Label()
label2.config(text="Km")
label2.grid(row=1 , column=2)

#is equal to Label:
label3 = t.Label()
label3.config(text="is equal to")
label3.grid(row=1, column= 0)
#text output area:

output = t.Label(text=0)
output.config(height=1 ,width=5)
output.grid(row=1, column=1 , padx=20 , pady=20)


#calculate button:
button = t.Button()
button.grid(row=3,column=1)
button.config(command= convert , text="Calculate")



window.mainloop()

