# Name: Mark Haskins
# Date: 2/8/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assignment 0502_ Cups and Dice
# Link to youtube video: https://youtu.be/3o2ZCMd8qo4 

from random import choice, randint
from statistics import mean 
class SixSidedDie:
    '''class that represents a six sided die'''
    sides = list(range(1, 7))

    def __init__(self, value=0):
        '''method to initialize value of a die'''
        self.v = value

    def roll(self):
        '''method to return randomly chosen value from a side of a die'''
        self.v = choice(self.sides)
        return self.v

    def getFaceValue(self):
        '''method to return current face value of a die'''
        return self.v

    def __repr__(self):
        '''canonical string representation of SixSidedDie'''
        return self.__class__.__name__+'({})' .format(self.v)

class TenSidedDie(SixSidedDie): 
    '''a subclass of six sided die that represents a ten sided die'''
    sides = list(range(1, 11))

class TwentySidedDie(SixSidedDie):
    '''a subclass of six sided die that represents a twenty sided die'''  
    sides = list(range(1, 21))

class Cup:
    '''class that represents a cup that holds any number of 6, 10, or 20 sided die'''
    def __init__(self, num6=1, num10=1, num20=1):
        '''method to initialize the number of dice in a cup'''
        self.cup = []                                       #empty list 
        for i in range(num6):
            self.cup.append(SixSidedDie())              
        for i in range(num10):
            self.cup.append(TenSidedDie())
        for i in range(num20):
            self.cup.append(TwentySidedDie())

    def roll(self):
        '''method to roll all the dice in the cup'''
        for die in self.cup:
            die.roll()
        return self.cup

    def getSum(self):
        '''method to return sum of values of the dice in the cup'''
        return sum(die.v for die in self.cup)           

    def __repr__(self):
        '''canonical string representation of Cup'''
        return self.__class__.__name__+'({})' .format(self.cup)

class User(): 
    '''class to represent a user playing the cup and dice game'''
    currentBalance = 100                            #current balance is set to 100 at initalization 

    def __init__(self, n=''):
        '''method to initialize name of a user'''
        self.name = n
    
    def updateBalance(self, num):
        '''method to update user's balance'''
        self.number = num
        self.currentBalance += self.number
        return self.currentBalance

    def goal(self):
        '''method to generate user's goal number'''
        self.gNum = randint(1,100)
        print(f"Your goal number is {self.gNum}")
        return self.gNum

    def bet(self):
        '''method to prompt user for bet amount'''
        while True:
            self.betAmount = int(input("How much money would you like to bet: "))
            if self.betAmount < 0:
                print("You cannot bet a negative number. Please try again.")        #per quesetion, can't bet a negative number to game the system.
                continue
            elif self.betAmount <= self.currentBalance:                                #check to make sure bet amount is not greater than currrent balance 
                return self.betAmount
            else:
                print(f"Bet amount, {self.betAmount}, exceeds current balance {self.currentBalance}.\n Please try another amount.")
    
    def diceGameInput(self):
        '''method to get dice game input'''
        self.n6 = int(input("How many 06 sided die do you want to roll? (Please enter an integer): "))
        self.n10 = int(input("How many 10 sided die do you want to roll? (Please enter an integer): "))
        self.n20 = int(input("How many 20 sided die do you wnat to roll? (Please enter an integer): "))
        return self.n6, self.n10, self.n20
    
    def diceGame(self, n6, n10, n20):
        '''method to initialize a single dice game'''
        self.gameCup = Cup(n6,n10,n20)
        self.gameCupRoll = self.gameCup.roll()          #composition example - calling roll() from Cup class
        self.gameCupSum = self.gameCup.getSum()         #composition example - calling getsum() from Cup class
        self.gameBalanceLogic()
        self.displayResults()
        return self.gameCupSum, self.gameCupRoll

    def gameBalanceLogic(self):
        '''method to update user balance based upon game logic'''
        if self.gameCupSum == self.gNum:
            print(f"You won: {(10*self.betAmount)+self.betAmount}")
            self.updateBalance((10*self.betAmount)+self.betAmount)
        elif self.gameCupSum in range(self.gNum-3,self.gNum):    
            print(f"You won: {(5*self.betAmount)+self.betAmount}")
            self.updateBalance((5*self.betAmount)+self.betAmount)
        elif self.gameCupSum in range(self.gNum-10,self.gNum):
            print(f"You won: {(2*self.betAmount)+self.betAmount}")
            self.updateBalance((2*self.betAmount)+self.betAmount)
        else:
            print("You did not win any money.")

    def displayResults(self):
        '''method ot display user balance and game results'''
        print(f"{self.name}, your goal number was {self.gNum}")
        print(f"These are the values of each die in your cup:\n {self.gameCupRoll}")
        print(f"This is the sum of the values in your cup:\n {self.gameCupSum}")
        print(f"Your current balance:\n {self.currentBalance}")

def getInput():
    '''method to get user input'''
    name = input("Please enter your name: ")
    return name 

def playGame(user):
    '''method to prompt user to continue game'''
    if user.currentBalance == 0:                        #game will exit if current balance reaches zero
        return False
    answer =input("Would you like to play this game?: (Y/N): ")
    if answer == 'Y':
        return True
    elif answer == 'N':
        return False 

def main():
    '''main method to start game'''
    print("Hello. This is a Cups and Dice game. Please follow the prompts to continue.")
    name = getInput()
    user = User(name)                                   # initialize user based upon name received in input 
    while(playGame(user)):                              #
        betAmount = user.bet()
        user.goal()
        user.updateBalance(betAmount*-1)                #use of -1 to subtract bet amount from current balance
        n6, n10, n20 = user.diceGameInput()
        user.diceGame(n6,n10,n20)
    print("Game over")

main()

