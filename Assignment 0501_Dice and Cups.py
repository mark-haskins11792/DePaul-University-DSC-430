# Name: Mark Haskins
# Date: 2/8/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assignment 0501_Dice and Cups
# Link to youtube video: https://youtu.be/NbQ4nZIGy_Y
from random import choice


class SixSidedDie:
    '''class that represents a six sided die'''
    sides = list(range(1, 7))

    # Overloaded Constructor
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


class TenSidedDie(SixSidedDie):  # Extend SixSidedDie
    '''a subclass of six sided die that represents a ten sided die'''
    sides = list(range(1, 11))


class TwentySidedDie(SixSidedDie):  # Extended SixSidedDie
    '''a subclass of six sided die that represents a twenty sided die'''
    sides = list(range(1, 21))


class Cup:
    '''class that represents a cup that holds any number of 6, 10, or 20 sided die'''
    def __init__(self, num6=1, num10=1, num20=1):
        '''method to initialize the number of dice in a cup'''
        self.cup = []                                   #empty list
        for i in range(num6):
            self.cup.append(SixSidedDie())              #append and initialize 6, 10, and 20 sided die objects per inputed range
        for i in range(num10):
            self.cup.append(TenSidedDie())
        for i in range(num20):
            self.cup.append(TwentySidedDie())           #composition of six sided die class by intializing 6, 10, 20 sided die objects and appending them to a list contained within the Cup Class. 

    def roll(self):
        '''method to roll all the dice in the cup'''
        for die in self.cup:
            die.roll()                              #composition of six sided die class by calling die.roll() method within Cup class
        return self.cup

    def getSum(self):
        '''method to return sum of values of the dice in the cup'''
        return sum(die.v for die in self.cup)           #general expression to sum all attributes v in the list of objects inside cup

    def __repr__(self):
        '''canonical string representation of Cup'''
        return self.__class__.__name__+'({})' .format(self.cup)


def main():
    '''Main method to display different classes, objects, methods, and constructors'''
    d6= SixSidedDie()       
    print("Default Six Sided Die Constructor:")
    print(d6)                        
    d20 = TwentySidedDie(19)
    print("\nOverloaded Constructor Twenty Sided Die:")  
    print(d20)
    print("\nTwenty Sided Die Roll:")                        
    print(d20.roll()) 
    d10 = TenSidedDie()  
    print("\nTen Sided Die Default Value:")      
    print(d10.getFaceValue()) 
    print("\nDefault Cup Constructor")
    cup = Cup()
    print(cup)
    print("\nOverloaded Cup Cnstructor")
    cup1 = Cup(4,2,2)
    print(cup1)
    print("\nCup 1 roll method:")
    print(cup1.roll())
    print("\nCup 1 getSum Method:")
    print(cup1.getSum())
    
main()
