from tkinter import *
from tkinter import ttk
from random import randint

def roll_dice(self,dice):
    throw = [randint(1,6) for x in range(5)]
    die1 = show_die(dice[0],throw[0])
    die2 = show_die(dice[1],throw[1])
    die3 = show_die(dice[2],throw[2])
    die4 = show_die(dice[3],throw[3])
    die5 = show_die(dice[4],throw[4])
    die1.grid(row=1, column=0)
    die2.grid(row=1, column=1)
    die3.grid(row=1, column=2)
    die4.grid(row=3, column=0)
    die5.grid(row=3, column=1)

def show_die(d,a):
    print(type(d[1].get()))
    if(d[1].get()) == True:
        return d
    if a == 1:
        return Checkbutton(root, image=die_image, height=150, width=150, bg='green')
    elif a == 2:
        return Checkbutton(root, image=die_image2, height=150, width=150, bg='green')
    elif a == 3:
        return Checkbutton(root, image=die_image3, height=150, width=150, bg='green')
    elif a == 4:
        return Checkbutton(root, image=die_image4, height=150, width=150, bg='green')
    elif a == 5:
        return Checkbutton(root, image=die_image5, height=150, width=150, bg='green')
    elif a == 6:
        return Checkbutton(root, image=die_image6, height=150, width=150, bg='green')

root = Tk()
root.configure(background='Green')
TheLabel = Label(root, text='testing, one, two, three')
TheLabel.configure(background='Green')
root.geometry("%dx%d+0+0" %(800,600))
die_image = PhotoImage(file="die1.png")
die_image2 = PhotoImage(file="die2.png")
die_image3 = PhotoImage(file="die3.png")
die_image4 = PhotoImage(file="die4.png")
die_image5 = PhotoImage(file="die5.png")
die_image6 = PhotoImage(file="die6.png")


rollButton = Button(text='Roll the dice', height=4,width=10)
rolls_left = Label(text='Throws left:')


def generate_dice():
    var0 = BooleanVar()
    var1 = BooleanVar()
    var2 = BooleanVar()
    var3 = BooleanVar()
    var4 = BooleanVar()
    die1 = Checkbutton(root, image = die_image,height=150, width=150,bg='green',  variable  = var0)
    die2 = Checkbutton(root, image = die_image2,height=150, width=150,bg='green', variable  = var1)
    die3 = Checkbutton(root, image = die_image3,height=150, width=150,bg='green', variable  = var2)
    die4 = Checkbutton(root, image = die_image4,height=150, width=150,bg='green', variable  = var3)
    die5 = Checkbutton(root, image = die_image5,height=150, width=150,bg='green', variable  = var4)
    dice = []
    dice.append((die1,var0))
    dice.append((die2,var1))
    dice.append((die3,var2))
    dice.append((die4,var3))
    dice.append((die5,var4))
    return dice
dice = generate_dice()
#TheLabel.pack()
dice[0][0].grid(row=1,column=0)
dice[1][0].grid(row=1,column=1)
dice[2][0].grid(row=1,column=2)
dice[3][0].grid(row=3,column=0)
dice[4][0].grid(row=3,column=1)
rollButton.grid(row=4,column=1)
rolls_left.grid(row=4,column=2)
rollButton.bind("<Button-1>",lambda event: roll_dice(event,dice))
root.mainloop()

#self.canvas.bind('<Button-1>',lambda event: self.someFunction(event,"Hello"))
