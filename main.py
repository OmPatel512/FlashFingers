from tkinter import *

#TODO -1 Make Sample Text File

#TODO -2 Connect Sample text File with program

with open("Sample Texts.txt") as data:
    text = data.read()


#TODO -3 Make GUI Using tkinter

window = Tk()
window.title("FlashFingers")
window.minsize(800,600)


window.mainloop()
print(text)
