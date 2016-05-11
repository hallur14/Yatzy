from tkinter import *
from tkinter import ttk
from random import randint

root = Tk()
root.configure(background='Green')
TheLabel = Label(root, text='testing, one, two, three')
TheLabel.configure(background='Green')
root.geometry("%dx%d+0+0" %(800,600))

class Die1:
    value = 1
    img = PhotoImage(file="die1.png")
    die_image = PhotoImage(file="die1.png")
    Checkbutton(root, image = die_image,height=150, width=150,bg='green', offvalue=0)
class Die2:
    value = 2
    img = PhotoImage(file="die2.png")

class Die3:
    value = 3
    img = PhotoImage(file="die3.png")

class Die4:
    value = 4
    img = PhotoImage(file="die4.png")

class Die5:
    value = 5
    img = PhotoImage(file="die5.png")

class Die6:
    value = 6
    img = PhotoImage(file="die6.png")

die0 = Die1()
die1 = Die2()
die2 = Die3()
die3 = Die4()
die4 = Die5()


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

root.mainloop()
