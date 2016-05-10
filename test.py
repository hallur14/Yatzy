from tkinter import *
from tkinter import ttk
from random import randint

def roll_dice(event):
    throw = [randint(1,6) for x in range(5)]
    print(throw)
    dye1 = show_dye(throw[0])
    dye2 = show_dye(throw[1])
    dye3 = show_dye(throw[2])
    dye4 = show_dye(throw[3])
    dye5 = show_dye(throw[4])
    dye1.grid(row=1, column=0)
    dye2.grid(row=1, column=1)
    dye3.grid(row=1, column=2)
    dye4.grid(row=3, column=0)
    dye5.grid(row=3, column=1)
def show_dye(a):
    if a == 1:
        return Checkbutton(root, image=dye_image, height=150, width=150, bg='green')
    elif a == 2:
        return Checkbutton(root, image=dye_image2, height=150, width=150, bg='green')
    elif a == 3:
        return Checkbutton(root, image=dye_image3, height=150, width=150, bg='green')
    elif a == 4:
        return Checkbutton(root, image=dye_image4, height=150, width=150, bg='green')
    elif a == 5:
        return Checkbutton(root, image=dye_image5, height=150, width=150, bg='green')
    elif a == 6:
        return Checkbutton(root, image=dye_image6, height=150, width=150, bg='green')
root = Tk()
root.configure(background='Green')
TheLabel = Label(root, text='testing, one, two, three')
TheLabel.configure(background='Green')
root.geometry("%dx%d+0+0" %(800,600))
dye_image = PhotoImage(file="dye.png")
dye_image2 = PhotoImage(file="dye.png")
dye_image3 = PhotoImage(file="dye3.png")
dye_image4 = PhotoImage(file="dye.png")
dye_image5 = PhotoImage(file="dye5.png")
dye_image6 = PhotoImage(file="dye6.png")


rollButton = Button(text='Roll the dice', height=4,width=10)
rolls_left = Label(text='Throws left:')
#label = Label(root,image=dye_image)
#label.pack()
dye1 = Checkbutton(root, image = dye_image,height=150, width=150,bg='green')
dye2 = Checkbutton(root, image = dye_image2,height=150, width=150,bg='green')
dye3 = Checkbutton(root, image = dye_image3,height=150, width=150,bg='green')
dye4 = Checkbutton(root, image = dye_image4,height=150, width=150,bg='green')
dye5 = Checkbutton(root, image = dye_image5,height=150, width=150,bg='green')

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

