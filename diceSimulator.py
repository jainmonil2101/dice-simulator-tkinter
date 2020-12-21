from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Roll Dice Simulator")
root.geometry("400x375")
root.resizable(False, False)

EMPTY_LABEL = Label(root, font=("Verdana, 5"))
EMPTY_LABEL.pack()

label = Label(root, text="Roll Dice Simulator", font=("Serif", 20, "bold"), fg="green")
label.pack()


dice = ["die1.PNG", "die2.PNG", "die3.PNG", "die4.PNG", "die5.PNG", "die6.PNG"]
img = ImageTk.PhotoImage(Image.open(random.choice(dice)))

image_label = Label(root, image=img)
image_label.place(relx = 0.5, rely = 0.45, anchor = CENTER)

def rollTheDice():
    img = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    image_label.configure(image=img)
    
    image_label.image = img
    
    


button = Button(root, text="Roll The Dice", font=("Verdana", 9), fg="blue", command=rollTheDice)
button.place(relx = 0.5, rely = 0.84, anchor = CENTER)


root.mainloop()