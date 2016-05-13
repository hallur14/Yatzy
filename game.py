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

        #Label Messages
        self.infoMessage = StringVar()
        self.infoMessage.set('Press ROLL to get your dice!')
        self.turnMessage = StringVar()
        self.turnMessage.set('You have ' + str(self.player1.throwsLeft) + ' remaining rolls this turn')

        #Labels
        infoLabel1 = Label(self, textvariable=self.infoMessage, font=('Verdana', 12), fg="green")
        infoLabel1.place(x=240, y=25)
        turnLabell = Label(self, textvariable=self.turnMessage, font=('Verdana', 12))
        turnLabell.place(x=40, y=720)

        #This button rolls the dice and displays the dice afterwards
        self.rollBtn = Button(self, text='ROLL', height=1, width=15, command=self.roll, font=('Verdana', 14), fg='white',
                         bg='brown')
        self.rollBtn.place(x=40, y=20)

        #This button stops the current turn and sets remaing rolls to 0
        self.stopBtn = Button(self, text='STOP', height=1, width=15, command=self.stop, font=('Verdana', 14), fg='white',
                         bg='red')
        self.stopBtn.place(x=40, y=60)

    #This functions displays the state of the current dice
    def displayDice(self):
        self.infoMessage.set('Select which dies to keep and ROLL again or press STOP')

        if self.player1.throwsLeft == 0:
            self.turnMessage.set('You have ' + str(self.player1.throwsLeft) + ' remaining rolls this turn')
            self.infoMessage.set('Now select an option on the scorecard')
            for n, i in enumerate(self.player1.currentDice):
                check = Checkbutton(self, image=self.dice[i.value], height=100, width=100)
                check.place(x=35, y=(n*120)+115)
        else:
            self.turnMessage.set('You have ' + str(self.player1.throwsLeft) + ' remaining rolls this turn')
            for n, i in enumerate(self.player1.currentDice):
                var = BooleanVar()
                var.set(int(i.hold))

                check = Checkbutton(self, image=self.dice[i.value], selectimage=self.diceH[i.value], height=100,
                                    width=100, variable = var, command = i.switch)
                check.place(x=35, y=(n*120)+115)
                check.var = var

    #This functions creates a dictionary of textures used
    def gen_dice_images(self):
        self.dice = {
            i+1 : PhotoImage(file=os.path.join('DiceTextures', 'white', '%s.png' % (i+1)))
            for i in range(6)
        }
        self.diceH = {
            i+1 : PhotoImage(file=os.path.join('DiceTextures', 'blue', '%s.png' % (i+1)))
            for i in range(6)
        }

    #This function gets new die values for unmarked dice
    def roll(self):
        if not self.player1.throwsLeft == 0:
            self.player1.PlayerRoll()

        self.displayDice()

        if self.player1.throwsLeft == 0:
            self.rollBtn.config(state='disabled')
            self.turnMessage.set('You are out off rolls this round!')
            for n, i in enumerate(self.player1.currentDice):
                i.hold = False
            self.displayDice()

    #This function stops the current turn and sets remaing rolls to 0
    def stop(self):
        self.player1.throwsLeft = 0
        self.roll()
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
        self.throwsLeft = 3
        self.currentDice = []
        self.selectedDice = []

        for i in range(5):
            self.currentDice.append(Die(i))

    def PlayerRoll(self):
        self.throwsLeft -= 1
        for i in self.currentDice:
            #print(i.hold)
            if not i.hold:
                i.value = i.getOneNum()

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