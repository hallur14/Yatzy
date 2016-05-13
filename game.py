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
        self.infoMessage.set('Press Roll to get your dice')
        self.turnMessage = StringVar()
        self.turnMessage.set('Turns left: ' + str(self.player1.throwsLeft+1))

        #Labels
        infoLabel1 = Label(self, textvariable=self.infoMessage, font=('Verdana', 12))
        infoLabel1.place(x=240, y=15)
        turnLabell = Label(self, textvariable=self.turnMessage, font=('Verdana', 12))
        turnLabell.place(x=40, y=700)

        rollBtn = Button(self, text='Roll', height=1, width=15, command=self.roll, font=('Verdana', 14))
        rollBtn.place(x=40, y=10)


    def displayDice(self):
        self.infoMessage.set('Select which dies to keep and Roll again')
        self.turnMessage.set('Turns left: ' + str(self.player1.throwsLeft+1))
        for n, i in enumerate(self.player1.currentDice):
            var = BooleanVar()
            var.set(int(i.hold))
            #print(i.hold,var.get())

            check = Checkbutton(self, image=self.dice[i.value], selectimage=self.diceH[i.value], height=110, width=110,
                                variable = var, command = i.switch)
            check.place(x=20, y=(n*120)+70)
            check.var = var

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
            #print(i.hold)
            if not i.hold:
                i.value = i.getOneNum()
        self.throwsLeft -= 1
        #print(YatziValidor.aces(self))

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
        return False

    def twoPair(self):
        return False

    def threeOfaKind(self):
        return False

    def fourOfaKind(self):
        return False

    def littleRow(self):
        return (self.currentDice == list(range(1, 6)))

    def big_row(self):
        (self.currentDice == list(range(2, 7)))

    def fullHouse(self):
        return False

app = game()
app.geometry("%dx%d+0+0" %(1024,768))
app.resizable(width=False, height=False)
app.mainloop()
