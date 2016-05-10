from tkinter import *
from tkinter import ttk
from random import randint

def roll_dice(event):
    throw = [randint(1,6) for x in range(5)]
    print(throw)
    dye1 = Checkbutton(root, image=dye_image, height=150, width=150, bg='green')
    dye2 = Checkbutton(root, image=dye_image, height=150, width=150, bg='green')
    dye3 = Checkbutton(root, image=dye_image, height=150, width=150, bg='green')
    dye4 = Checkbutton(root, image=dye_image, height=150, width=150, bg='green')
    dye5 = Checkbutton(root, image=dye_image, height=150, width=150, bg='green')

root = Tk()
root.configure(background='Green')
TheLabel = Label(root, text='testing, one, two, three')
TheLabel.configure(background='Green')
root.geometry("%dx%d+0+0" %(800,600))
dye_image = PhotoImage(file="dye.png")
for i in range(50):
    print(randint(1,6))
rollButton = Button(text='Roll the dice', height=4,width=10)
rolls_left = Label(text='Throws left:')
#label = Label(root,image=dye_image)
#label.pack()
dye1 = Checkbutton(root, image = dye_image,height=150, width=150,bg='green')
dye2 = Checkbutton(root, image = dye_image,height=150, width=150,bg='green')
dye3 = Checkbutton(root, image = dye_image,height=150, width=150,bg='green')
dye4 = Checkbutton(root, image = dye_image,height=150, width=150,bg='green')
dye5 = Checkbutton(root, image = dye_image,height=150, width=150,bg='green')

#TheLabel.pack()
dye1.grid(row=1,column=0)
dye2.grid(row=1,column=1)
dye3.grid(row=1,column=2)
dye4.grid(row=3,column=0)
dye5.grid(row=3,column=1)
dye1.config(bg='green')
rollButton.grid(row=4,column=1)
rolls_left.grid(row=4,column=2)
rollButton.bind("<Button-1>", roll_dice)
#dye1.config(image=d,compound=RIGHT)
root.mainloop()

