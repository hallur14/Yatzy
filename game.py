import tkinter as tk
from tkinter import *
from random import randint
import os

class game(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        frame = MainWindow(container, self)
        self.frames[MainWindow] = frame
        frame.grid(row=0, sticky='nsew')
        self.show_frame(MainWindow)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.gen_dice_images()
        self.player1 = Player()

        self.infoMessage = StringVar()
        self.infoMessage.set('Press roll to get your first set of Dices')

        infoLabel1 = Label(self, textvariable=self.infoMessage)
        rollsLeft = Label(text='Throws left: ')
        infoLabel1.place(x=150, y=10)
        rollBtn = Button(self, text='Roll', height=1, width=14, command=self.roll)
        rollBtn.place(x=40, y=10)
        rollsLeft.place(x=150, y=30)


    def displayDice(self):
        self.infoMessage.set('Select which dies to keep and Roll again')
        for n, i in enumerate(self.player1.currentDice):
            var = BooleanVar()
            var.set(int(i.hold))
            print(i.hold,var.get())

            check = Checkbutton(self, image=self.dice[i.value], selectimage=self.diceH[i.value], height=110, width=110,
                                variable = var, command = i.switch)
            #varList.append(var)

            check.place(x=20, y=(n*120)+40)
            check.var = var
            #var.set(i.hold)

    def gen_dice_images(self):
        self.dice = {
            i+1 : PhotoImage(file=os.path.join('DiceTextures', 'white', '%s.png' % (i+1)))
            for i in range(6)
        }
        self.diceH = {
            i+1 : PhotoImage(file=os.path.join('DiceTextures', 'blue', '%s.png' % (i+1)))
            for i in range(6)
        }

    def roll(self):
        self.player1.PlayerRoll()
        self.displayDice()

class Die(object):
    def __init__(self, id):
        self.id = id
        self.getOneNum()
        self.hold = BooleanVar()
        self.hold = False

    def getOneNum(self):
        self.value = randint(1, 6)
        return self.value

    def __str__(self):
        return str(self.value)

    def switch(self):
        self.hold = not self.hold

class Player(object):
    def __init__(self):
        self.score = 0
        self.turnsLeft = 15
        self.throwsLeft = 2
        self.currentDice = []
        self.selectedDice = []

        for i in range(5):
            self.currentDice.append(Die(i))

    def PlayerRoll(self):
        for i in self.currentDice:
            print(i.hold)
            if not i.hold:
                i.value = i.getOneNum()
        self.throwsLeft -= 1
        print(YatziValidor.aces(self))
class YatziValidor(object):
    NUMBER_OF_TURNS = 15

    def aces(self):
        return sum(i.value for i in self.currentDice if i.value == 1)

    def deuces(self):
        return sum(i.value for i in self.currentDice if i.value == 2)

    def threes(self):
        return sum(i.value for i in self.currentDice if i.value == 3)

    def fours(self):
        return sum(i.value for i in self.currentDice if i.value == 4)

    def fives(self):
        return sum(i.value for i in self.currentDice if i.value == 5)

    def sixes(self):
        return sum(i.value for i in self.currentDice if i.value == 6)

    def pair(self):

    def twoPair(self):

    def threeOfaKind(self):

    def fourOfaKind(self):

    def littleRow(self):
        return (self.currentDice == list(range(1, 6)))
    def big_row(self):
        (self.currentDice == list(range(2, 7)))
    def fullHouse(self):


'''

Player1 = Player()
for i in Player1.currentDice:
   print(i)

'''
app = game()
app.geometry("%dx%d+0+0" %(1024,768))
app.resizable(width=False, height=False)
app.mainloop()






