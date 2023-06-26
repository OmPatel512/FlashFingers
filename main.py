from tkinter import *
import time
import threading
import random

class FlashFingersGUI:


    def __int__(self):
        self.root = Tk()
        self.root.title("FlashFingers")
        self.root.geometry("800x600")

        self.texts = open("sample Texts.txt", "r").read().split("\n")

        self.frame = Frame(self.root)

        self.sample_label = Label(self.frame, text=random.choice(self.texts),font=("Helvetica", 15))
        self.sample_label.grid(row=0,column=0,columnspan=2,padx=5,pady=10)

        self.input_entry = Entry(self.frame, width=40, font=("Helvetica",18))
        self.input_entry.grid(row=1,column=0,columnspan=2,padx=5,pady=10)
        self.input_entry.bind("<KeyDown>", self.start)

        self.speed_label = Label(self.frame, text="Speed:\n 0.00 WPM", font=("Helvetica", 15))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = Button(self.frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = True

        self.root.mainloop()


