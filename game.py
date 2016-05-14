import tkinter as tk
from tkinter import *
from random import randint
import os

scoreBoardFontSize = 9

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

        scoreBoardFontSize = 10
        scoreBoardBtnXcord = 200
        scoreBoardLabelXcord = 330

        self.gen_dice_images()
        self.player1 = Player()
        self.startDice()

        #Label Messages
        self.infoMessage = StringVar()
        self.infoMessage.set('Press ROLL to get your dice!')
        self.turnMessage = StringVar()
        self.turnMessage.set('You have ' + str(self.player1.throwsLeft) + ' remaining rolls this turn')

        #Labels
        infoLabel1 = Label(self, textvariable=self.infoMessage, font=('Verdana', 11), fg="green")
        infoLabel1.place(x=200, y=25)
        turnLabell = Label(self, textvariable=self.turnMessage, font=('Verdana', 11))
        turnLabell.place(x=40, y=690)

        #This button rolls the dice and displays the dice afterwards
        self.rollBtn = Button(self, text='ROLL', height=1, width=11, command=self.roll, font=('Verdana', 14), fg='white',
                         bg='brown')
        self.rollBtn.place(x=40, y=20)

        #This button restarts your game
        self.restartBtn = Button(self, text='Restart', height=5, width=3, command=self.roll, font=('Verdana', 14), fg='white',
                         bg='brown')
        self.restartBtn.place(x=460, y=90)

        #This section has buttons and labels for the scoreboard
        self.acesBtn = Button(self, text='Aces', height=1, width=13, command=self.validateAces, font=('Verdana', scoreBoardFontSize), fg='black', bg='white')
        self.acesBtn.place(x=200, y=90)
        self.acesMsg = StringVar()
        self.acesMsg.set('0')
        self.acesLabel = Label(self, font=('Verdana', 12), width=10, textvariable=self.acesMsg, fg="black", bg='white')
        self.acesLabel.place(x=scoreBoardLabelXcord, y=90)


        self.deucesBtn = Button(self, text='Deuces', height=1, width=13, font=('Verdana', scoreBoardFontSize), fg='black', bg='white')
        self.deucesBtn.place(x=scoreBoardBtnXcord, y=120)
        self.deucesLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.deucesLabel.place(x=scoreBoardLabelXcord, y=120)

        self.threesBtn = Button(self, text='Threes', height=1, width=13, font=('Verdana', scoreBoardFontSize), fg='black', bg='white')
        self.threesBtn.place(x=scoreBoardBtnXcord, y=150)
        self.threesLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.threesLabel.place(x=scoreBoardLabelXcord, y=150)

        self.fouresBtn = Button(self, text='Foures', height=1, width=13,font=('Verdana', scoreBoardFontSize), fg='black',
                         bg='white')
        self.fouresBtn.place(x=scoreBoardBtnXcord, y=180)
        self.fouresLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.fouresLabel.place(x=scoreBoardLabelXcord, y=180)

        self.fivesBtn = Button(self, text='Fives', height=1, width=13, font=('Verdana', scoreBoardFontSize), fg='black',
                         bg='white')
        self.fivesBtn.place(x=scoreBoardBtnXcord, y=210)
        self.fivesLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.fivesLabel.place(x=scoreBoardLabelXcord, y=210)

        self.sixesBtn = Button(self, text='Sixes', height=1, width=13, font=('Verdana', scoreBoardFontSize), fg='black',
                         bg='white')
        self.sixesBtn.place(x=scoreBoardBtnXcord, y=240)
        self.sixesLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.sixesLabel.place(x=scoreBoardLabelXcord, y=240)

        self.sumBtn = Button(self, text='Sum', height=1, width=13, state='disabled',font=('Verdana', scoreBoardFontSize),
                             fg='black', bg='white')
        self.sumBtn.place(x=scoreBoardBtnXcord, y=270)
        self.sumLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.sumLabel.place(x=scoreBoardLabelXcord, y=270)

        self.bonusBtn = Button(self, text='Bonus', height=1, width=13, state='disabled', font=('Verdana', scoreBoardFontSize),
                               fg='black', bg='white')
        self.bonusBtn.place(x=scoreBoardBtnXcord, y=300)

        self.bonusLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.bonusLabel.place(x=scoreBoardLabelXcord, y=300)
        self.onePairBtn = Button(self, text='One Pair', height=1, width=13, font=('Verdana', scoreBoardFontSize), fg='black',
                         bg='white')
        self.onePairBtn.place(x=scoreBoardBtnXcord, y=330)
        self.onePairLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.onePairLabel.place(x=scoreBoardLabelXcord, y=330)

        self.twoPairBtn = Button(self, text='Two Pair', height=1, width=13, font=('Verdana', scoreBoardFontSize), fg='black',
                         bg='white')
        self.twoPairBtn.place(x=scoreBoardBtnXcord, y=360)

        self.twoPairLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.twoPairLabel.place(x=scoreBoardLabelXcord, y=360)

        self.threeOfKindBtn = Button(self, text='Three of a kind', height=1, width=13, font=('Verdana', scoreBoardFontSize), fg='black',
                         bg='white')
        self.threeOfKindBtn.place(x=scoreBoardBtnXcord, y=390)
        self.threeOfaKindLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.threeOfaKindLabel.place(x=scoreBoardLabelXcord, y=390)

        self.fourOfKindBtn = Button(self, text='Four of a kind', height=1, width=13, font=('Verdana', scoreBoardFontSize), fg='black',
                         bg='white')
        self.fourOfKindBtn.place(x=scoreBoardBtnXcord, y=420)
        self.fourOfaKindLabael = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.fourOfaKindLabael.place(x=scoreBoardLabelXcord, y=420)

        self.smallStraightBtn = Button(self, text='Small Straight', height=1, width=13, font=('Verdana', scoreBoardFontSize), fg='black',
                         bg='white')
        self.smallStraightBtn.place(x=scoreBoardBtnXcord, y=450)
        self.smallStraightLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.smallStraightLabel.place(x=scoreBoardLabelXcord, y=450)

        self.largeStraightBtn = Button(self, text='Large Straight', height=1, width=13, font=('Verdana', scoreBoardFontSize), fg='black',
                         bg='white')
        self.largeStraightBtn.place(x=scoreBoardBtnXcord, y=480)
        self.largeStraightLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.largeStraightLabel.place(x=scoreBoardLabelXcord, y=480)

        self.fullHouse = Button(self, text='Full House', height=1, width=13, font=('Verdana', scoreBoardFontSize), fg='black',
                         bg='white')
        self.fullHouse.place(x=scoreBoardBtnXcord, y=510)
        self.fullHouseLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.fullHouseLabel.place(x=scoreBoardLabelXcord, y=510)

        self.chanceBtn = Button(self, text='Chance', height=1, width=13, font=('Verdana', scoreBoardFontSize), fg='black',
                         bg='white')
        self.chanceBtn.place(x=scoreBoardBtnXcord, y=540)
        self.chanceLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.chanceLabel.place(x=scoreBoardLabelXcord, y=540)

        self.yatzyBtn = Button(self, text='Yatzi', height=1, width=13, font=('Verdana', scoreBoardFontSize), fg='black',
                         bg='white')
        self.yatzyBtn.place(x=scoreBoardBtnXcord, y=570)
        self.yatzyLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.yatzyLabel.place(x=scoreBoardLabelXcord, y=570)

        self.totalBtn = Button(self, text='Total', height=1, width=13, state='disabled', font=('Verdana', scoreBoardFontSize), fg='black',
                         bg='white')
        self.totalBtn.place(x=scoreBoardBtnXcord, y=600)
        self.totalLabel = Label(self, font=('Verdana', 12), width=10, fg="green", bg='white')
        self.totalLabel.place(x=scoreBoardLabelXcord, y=600)

    #This functions displays the state of the current dice
    def displayDice(self):
        self.infoMessage.set('Select which dice to keep and ROLL again')

        if self.player1.throwsLeft == 0:
            self.turnMessage.set('You have ' + str(self.player1.throwsLeft) + ' remaining rolls this turn')
            self.infoMessage.set('Now select an option on the scorecard')

        self.turnMessage.set('You have ' + str(self.player1.throwsLeft) + ' remaining rolls this turn')
        for n, i in enumerate(self.player1.currentDice):
            var = BooleanVar()
            var.set(int(i.hold))

            check = Checkbutton(self, image=self.dice[i.value], selectimage=self.diceH[i.value], height=100,
                                width=100, variable = var, command = i.switch)
            check.place(x=41, y=(n*120)+85)
            check.var = var

    #This functions creates a dictionary of textures used
    def gen_dice_images(self):
        self.dice = {
            i : PhotoImage(file=os.path.join('DiceTextures', 'white', '%s.png' % (i)))
            for i in range(7)
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

    def startDice(self):
        for i in range(5):
            check = Checkbutton(self, image=self.dice[0], height=100, width=100)
            check.place(x=41, y=(i*120)+85)

    def validateAces(self):
        print(YatziValidor.singleNumbers(self.player1.currentDice, 1))




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
        self.validator = YatziValidor()

        for i in range(5):
            self.currentDice.append(Die(i))

    def PlayerRoll(self):
        self.throwsLeft -= 1
        for i in self.currentDice:
            #print(i.hold)
            if not i.hold:
                i.value = i.getOneNum()

class YatziValidor(object):
    NUMBER_OF_TURNS = 15

    #def dice(self,currentDice):
    #    return [x.value for x in self.currentDice]

    def singleNumbers(currDice, number):
        currentDice = currDice
        #return currentDice[0].value

        return sum(i for i in [x.value for x in currentDice if x.value == number])

'''
    def topMatches(self, nrOfOccurrances,nrOfPairs):
        dice = YatziValidor.dice(self,self.currentDice)
        diceSet = set(dice)
        repetitions = [x for x in diceSet if dice.count(x) >= nrOfOccurrances]
        print(len(repetitions))
        if len(repetitions) == 2 and nrOfPairs == 2:
            return sum(repetitions)*2
        elif len(repetitions) >= 1 and nrOfPairs == 2:
            return max(repetitions) * 4
        else:
            return 0

    def pair(self):
        return YatziValidor.topMatches(self,2,1)

    def twoPair(self):
        if YatziValidor.topMatches(self,4,1):
            return YatziValidor.topMatches(self,4,1)
        elif YatziValidor.topMatches(self,2,2):
            print(YatziValidor.topMatches(self,2,2))

    def threeOfaKind(self):
        return YatziValidor.topMatches(self,3,1)

    def fourOfaKind(self):
        return YatziValidor.topMatches(self,4,1)

    def littleRow(self):
        if (YatziValidor.dice(self,self.currentDice) == list(range(1, 6))):
            return self.chance()

    def big_row(self):
        (self.currentDice == list(range(2, 7)))

    def fullHouse(self):
        return False

    def chance(self):
        return sum(i.value for i in self.currentDice)

    def yatzy(self):
        if len(set(self.currentDice)) <= 1:
            return 50
        else:
            return False
'''

app = game()
app.geometry("%dx%d+0+0" %(530,720))
app.resizable(width=False, height=False)
app.mainloop()