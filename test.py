from tkinter import *
from tkinter import ttk
from random import randint
import os



def roll_dice(self,dice):
    throw = [randint(1, 6) for x in range(5)]



    throw = [randint(1,6) for x in range(5)]
    die1 = show_die(dice[0],throw[0])
    die2 = show_die(dice[1],throw[1])
    die3 = show_die(dice[2],throw[2])
    die4 = show_die(dice[3],throw[3])
    die5 = show_die(dice[4],throw[4])
    die1[0].grid(row=2, column=0)
    die2[0].grid(row=3, column=0)
    die3[0].grid(row=4, column=0)
    die4[0].grid(row=5, column=0)
    die5[0].grid(row=6, column=0)

def show_die(d,a):
    if(d[1].get()) == True:
        return d
    if (d[1].get()) == 1:
        return d
    if a == 1:
        return (Checkbutton(root, image=dieImg1, selectimage=dieImg1_h, height=110, width=110, bg='green', variable=d[1], ), d[1])
    elif a == 2:
        return (Checkbutton(root, image=dieImg2, selectimage=dieImg2_h, height=110, width=110, bg='green', variable=d[1]), d[1])
    elif a == 3:
        return (Checkbutton(root, image=dieImg3, selectimage=dieImg3_h, height=110, width=110, bg='green', variable=d[1]), d[1])
    elif a == 4:
        return (Checkbutton(root, image=dieImg4, selectimage=dieImg4_h, height=110, width=110, bg='green', variable=d[1]), d[1])
    elif a == 5:
        return (Checkbutton(root, image=dieImg5, selectimage=dieImg5_h, height=110, width=110, bg='green', variable=d[1]), d[1])
    elif a == 6:
        return (Checkbutton(root, image=dieImg6, selectimage=dieImg6_h, height=110, width=110, bg='green', variable=d[1]), d[1])

root = Tk()
root.configure(background='Green')
TheLabel = Label(root, text='testing, one, two, three')
TheLabel.configure(background='Green')
root.geometry("%dx%d+0+0" %(1024,780))
dieImg1 = PhotoImage(file=os.path.join('DiceTextures', 'white', '1.png'))
dieImg2 = PhotoImage(file=os.path.join('DiceTextures', 'white', '2.png'))
dieImg3 = PhotoImage(file=os.path.join('DiceTextures', 'white', '3.png'))
dieImg4 = PhotoImage(file=os.path.join('DiceTextures', 'white', '4.png'))
dieImg5 = PhotoImage(file=os.path.join('DiceTextures', 'white', '5.png'))
dieImg6 = PhotoImage(file=os.path.join('DiceTextures', 'white', '6.png'))

dieImg1_h = PhotoImage(file=os.path.join('DiceTextures', 'blue', '1.png'))
dieImg2_h = PhotoImage(file=os.path.join('DiceTextures', 'blue', '2.png'))
dieImg3_h = PhotoImage(file=os.path.join('DiceTextures', 'blue', '3.png'))
dieImg4_h = PhotoImage(file=os.path.join('DiceTextures', 'blue', '4.png'))
dieImg5_h = PhotoImage(file=os.path.join('DiceTextures', 'blue', '5.png'))
dieImg6_h = PhotoImage(file=os.path.join('DiceTextures', 'blue', '6.png'))


rollButton = Button(text='Roll the dice', height = 1,width = 15,padx=10,pady=10)
rollsLeft = Label(text='Throws left:')

def generate_dice():
    var0 = BooleanVar()
    var1 = BooleanVar()
    var2 = BooleanVar()
    var3 = BooleanVar()
    var4 = BooleanVar()
    die1 = Checkbutton(root, image = dieImg1,height=110, width=110,bg='green', variable  = var0)
    die2 = Checkbutton(root, image = dieImg2,height=110, width=110,bg='green', variable  = var1)
    die3 = Checkbutton(root, image = dieImg3,height=110, width=110,bg='green', variable  = var2)
    die4 = Checkbutton(root, image = dieImg4,height=110, width=110,bg='green', variable  = var3)
    die5 = Checkbutton(root, image = dieImg5,height=110, width=110,bg='green', variable  = var4)
    dice = []
    dice.append((die1,var0))
    dice.append((die2,var1))
    dice.append((die3,var2))
    dice.append((die4,var3))
    dice.append((die5,var4))
    return dice
dice = generate_dice()
padCanvas = Canvas(root,height=10,width=0,bd=0,highlightthickness=0,relief='ridge')

rollButton.grid(row=1,column=0)
rollsLeft.grid(row=4,column=2)
padCanvas.grid(row=0,column=0)
rollButton.bind("<Button-1>",lambda event: roll_dice(event,dice))
root.mainloop()

#self.canvas.bind('<Button-1>',lambda event: self.someFunction(event,"Hello"))
