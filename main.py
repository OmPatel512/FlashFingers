import tkinter
from tkinter import *

prog_running = True


#TODO -1 Make Sample Text File

#TODO -2 Connect Sample text File with program

with open("Sample Texts.txt") as data:
    text = data.read()

#Converting text into list

text_elements = []
for i in text:
    text_elements.append(i)



#TODO -3 Make GUI Using tkinter

window = Tk()
window.title("FlashFingers")
window.minsize(800,600)

text_box = Text(height=10, width=64,font=('arial',17),padx=20)
text_box.insert(tkinter.END,chars=text)
text_box.grid(column=0,row=0)

text_entry = Entry()
text_entry.grid(column=0,row=1)

user_text = text_entry.get()


user_text_elements = []
for i in user_text:
    i = str(i)
    user_text_elements.append(i)


if user_text_elements[0] == text_elements[0]:
    text_entry.config(fg='green')

window.mainloop()

