from tkinter import *
from tkinter import ttk
from random import randint

root = Tk()
root.configure(background='Green')
TheLabel = Label(root, text='testing, one, two, three')
TheLabel.configure(background='Green')
root.geometry("%dx%d+0+0" %(800,600))

class Die(n):
    value = n
    img = PhotoImage(file="die1.png")
    die_image = PhotoImage(file="die1.png")
    Checkbutton(root, image = die_image,height=150, width=150,bg='green', offvalue=0)

die0 = Die(1)
die1 = Die(2)
die2 = Die(3)
die3 = Die(4)
die4 = Die(5)


rollButton = Button(text='Roll the dice', height=4,width=10)
rolls_left = Label(text='Throws left:')
die0.grid(row=1,column=0)
die1.grid(row=1,column=1)
die2.grid(row=1,column=2)
die3.grid(row=3,column=0)
die4.grid(row=3,column=1)
rollButton.grid(row=4,column=1)
rolls_left.grid(row=4,column=2)


#rollButton.bind("<Button-1>",lambda event: roll_dice(event,dice))
