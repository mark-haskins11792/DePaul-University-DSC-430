# Name: Mark Haskins
# Date: 3/18/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assignment 1001: Battle for Crymland
# Link to video: https://www.youtube.com/watch?v=qgeXorqKPzU

from random import choice, choices, randint, random
from uuid import uuid4  #uiud4 generates a unique id
cD = {'thief': [], 'detective': [], 'lt': [], 'heist': [], 'seizedWealth': 0,
      'jailCount': 0, 'jThieves': [], 'bribedDetectives': [], 'bDCount': 0, 'totalBribe': 0, 'MrBiggArrest':False}    
#global dictionary to keep track of characters and variables

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


class GameParameters:
    '''a class that represents the game parameters'''

    def __init__(self):
        '''function to initialize game parameters'''
        self.d = self.openFile()

    def getHeistCoef(self):
        '''function to get heist coef'''
        return self.d.get("heistCoef")

    def getNumThieves(self):
        '''function to get num theives'''
        return int(self.d.get("numThieves"))

    def getPromotionWealth(self):
        '''function to get promo wealth'''
        return self.d.get("promotionWealth")

    def getNumDetectives(self):
        '''function to get num detectives'''
        return int(self.d.get("numDetetectives"))

    def getSolveInit(self):
        '''function to get initial solve'''
        return self.d.get("solveInit")

    def getSolveCap(self):
        '''function to get solve cap'''
        return self.d.get("solveCap")

    def getJailedCriminals(self):
        '''function to get jailed criminals'''
        return self.d.get("jailedCriminals")

    def getInitialWealthSeizure(self):
        '''function to get initial wealth'''
        return self.d.get("initialWealthSeizure")

    def getFollowingWealthSeizure(self):
        '''function to get additional wealth seizure'''
        return self.d.get("followingWealthSeizure")

    def getInitialBribe(self):
        '''function to get initial bribe'''
        return self.d.get("initialBribe")

    def getInitialDiscovery(self):
        '''function to get initial discovery probability'''
        return self.d.get("initialDiscovery")

    def getWeeks(self):
        '''function to get number of weeks'''
        return int(self.d.get("weeks"))

    def openFile(self):
        '''function to open file'''
        folder = "C:\\Users\\mhask\\OneDrive\\Documents\\Academics\\Depaul\\DSC430\\Assignments\\Assignment 1001_Battle for Crymland\\"
        fileName = "CrymlandParameterFile.txt"
        filePath = folder+fileName
        try:
            f = open(filePath, "r")
        except OSError as exception:
            print(exception)
        d = {}
        for line in f:
            lineList = f.read().splitlines()
            for i in lineList:
                key, val = i.split(" = ")           #store game parameters in a k,v dictionary using = as delimeter
                d[key] = float(val)
        return d


class Thief:
    '''a class the represents a theif'''

    def __init__(self, name="", lt=None):
        '''function to initialize thief'''
        self.name = name
        self.lt = lt
        self.pWealth = 0
        self.jailedCount = 0
        self.jailedBy = None
        self.weeklyHeist = 0
        self.arrested = False

    def getlt(self):
        '''function to return associated lt'''
        return self.lt

    def commmitHeist(self):
        '''function to commit a heist'''
        self.weeklyHeist = 0                #weeklyHeist is set back to 0 at run-time so I can generate weekly heist sum for Mr Bigg. 
        self.v = GameParameters().getHeistCoef()*TwentySidedDie().roll()**2             
        self.he = self.initHeist(self)
        self.he.updateHeistValue(self.v)
        self.updateWealth()
        self.kickUpWealth(self.v)
        self.weeklyHeist += self.v/2
        return self.v

    def updateWealth(self):
        '''function to update wealth'''
        self.pWealth += (self.v/2)
        return self.pWealth

    def kickUpWealth(self, kuw):
        '''function to kick up wealth to the LT'''
        global cD
        self.lt.pWealth += kuw

    def initHeist(self, th):                        #each heist object stored as a list in a dictionary. 
        '''function to initiate a heist'''
        global cD
        name = "Heist:" + str(uuid4())  
        h = Heist(name, th)
        cD['heist'].append(h)
        return h


class Lieutenant(Thief):
    '''a class that represents a lieutenant'''

    def receiveWealth(self, kuw):
        '''function to receive wealth'''
        self.pWealth = kuw
        return self.pWealth

class Detective():
    '''a class that represents a detective'''

    def __init__(self, name=""):
        '''function to initialize a detective'''
        self.name = name
        self.solveInit = GameParameters().getSolveInit()
        self.solveCap = GameParameters().getSolveCap()
        self.solvedCases = 0
        self.bribed = False
        self.pWealth = 0
        self.dp = GameParameters().getInitialDiscovery()

    def solveCase(self, h):
        '''function to solve a case'''
        self.heist = h
        if self.caseProbability() and not(self.bribed):
            global cD
            if cD['thief']:  # won't pop an empty list if there are no thieves 
                th = cD['thief'].pop(0)             #remove obj from theif list and append to jThief key list
                cD['jThieves'].append(th)           
                cD['jailCount'] += 1
                cD['seizedWealth'] += th.pWealth        #update the seized wealth
                self.updateSolvedCases()
                self.increaseSolveInit()
                self.updatePWealth(th.pWealth)

    def updateSolvedCases(self):
        '''function to update a solved case count'''
        self.solvedCases += 1

    def increaseSolveInit(self):
        '''function to increase initial solve parameter based upon rolle of 10 sided die'''
        x = TenSidedDie().roll()/100
        if (x + self.solveInit) < self.solveCap:
            self.solveInit += x

    def caseProbability(self):
        '''function to determine probability of solving a case, return true of false'''
        return True if random() < self.solveInit else False

    def updatePWealth(self, tw):
        '''function to update personal wealth'''
        self.pWealth += tw
        return self.pWealth

    def getBribed(self, lt, weeklySum):
        '''function to determine probability of getting bribed '''
        self.bA = weeklySum*GameParameters().getInitialBribe()  #set Bribe amount based upon weekly sum.
        if self.bA < 10000:
            p = .05
        elif self.bA < 100000:
            p = .1
        elif self.bA < 1000000:
            p = .25
        else:
            p = .50
        if self.bribeProbability(p):            
            self.bribed = True
            cD['totalBribe'] += self.bA

    def bribeProbability(self, p):
        '''function to generate bribe probablity, return true or false'''   #generate random bribe probability using random function which has a uniform distribution over [0,1]
        return True if random() < p else False                  #p sets the changes of returning true - this techique is utilized whenever a probablity is needed. 

    def increaseDiscovery(self):
        '''fuction to increase discovery attribute of detective'''
        if self.bribed:
            self.dp += TwentySidedDie().roll()/100
            if self.dProbability():
                if cD['detective']:
                    dt = cD['detective'].pop(0)
                    cD['bribedDetectives'].append(dt)       #remove the detetice and place in the bribed detective list
                    name = "Detective:" + str(uuid4())
                    dtn = Detective(name)
                    cD['detective'].append(dtn)             #initalize a new detective, always 3 detective working the week 
                    cD['bDCount'] += 1

    def dProbability(self):
        '''probability a detective will be discovered'''
        return True if random() < self.dp else False


class Heist():
    '''a class that represents a heist'''

    def __init__(self, name, th):
        '''function to initialize a heist'''
        self.name = name
        self.heistV = 0
        self.th = th

    def updateHeistValue(self, hv):
        '''function to update heist value'''
        self.heistV += hv
        return hv

def weekHeist(MrBigg, n, o):
    '''function to simulate a weekly heist'''
    outputResults(MrBigg, n, o)
    weeklySum = 0           #weekly sum is reset to zero at start of each week
    for th in cD['thief']:
        if th.pWealth < GameParameters().getPromotionWealth():      #if personal wealth greater than parameter, then theifs gets promoted 
            th.commmitHeist()
        else:
            promote(th)                                             #promote will initialize a new set of theives that will get used for the following week. 
    weeklySum = sum(th.weeklyHeist for th in cD['thief'])           #sum the week's heist
    for dt in cD['detective']:
        if dt.pWealth > GameParameters().getInitialWealthSeizure(): #logic to bribe the detective
            dt.getBribed(MrBigg, weeklySum)                         
            dt.increaseDiscovery()
        x = choices(cD['heist'], k=len(cD['detective']))            #detectives only choose random 3 cases to solve from a list of heists 
        h = x.pop()                                                 #pop one of the heists and have the detective solve it 
        dt.solveCase(h)
    count = 0
    for jT in cD['jThieves']:
        if jT.lt.name=="MrBigg":                    #if any of the jailed thieves lt name = Mr.Bigg then they will testify against him. 
            count+=1                                #increments count
    if count >  GameParameters().getJailedCriminals():
        cD['MrBiggArrest'] = True    #set MrBiggArrest to true to exit while loop.  
        return cD['MrBiggArrest']     

def outputResults(MrBigg, n, o):
    '''function to output results to a txt file'''
    o.write("Week Number: " + str(n) + "\n")
    o.write("MrBigg Personal Wealth: " + str(MrBigg.pWealth)+"\n")
    o.write("MrBigg Arrested: " + str(MrBigg.arrested)+"\n")
    o.write("Total Thieves: " + str(len(cD['thief']))+"\n")
    o.write("Total Detectives: " + str(len(cD['detective']))+"\n")
    o.write("Total Bribe Amount: " + str(cD['totalBribe'])+"\n")
    o.write("Total Lts: " + str(len(cD['lt']))+"\n")
    o.write("Total Jailed: " + str(cD['jailCount'])+"\n")
    o.write("Total Actors: " +
            str(len(cD['thief'])+len(cD['detective'])+len(cD['lt']))+"\n")
    o.write("----------\n")


def initThieves(lt):
    '''function to initialize thieves'''
    global cD
    for i in range(GameParameters().getNumThieves()):
        name = "Thief:" + str(uuid4())
        t = Thief(name, lt)
        cD['thief'].append(t)


def initDetectives(n=GameParameters().getNumDetectives()):
    '''function to initialize detectives'''
    global cD
    for i in range(n):
        name = "Detective:" + str(uuid4())
        dt = Detective(name)
        cD['detective'].append(dt)


def initLT(lt):
    '''function to initialize lt'''
    global cD
    name = "LT:" + str(uuid4())
    leu = Lieutenant(name, lt)
    cD['lt'].append(leu)


def promote(th):
    '''function to promote a thief to lt and initiliaze thieves'''
    global cD
    cD['thief'].remove(th)
    initLT(th)
    initThieves(th)


def main():
    '''main function to run the program'''
    d = GameParameters()  # set game parameters dictionary
    MrBigg = Lieutenant("MrBigg")  # initialize MrBigg as the first Lt
    global cD
    cD['lt'].append(MrBigg)  # update MrBigg in global Lt dict
    initThieves(MrBigg)  # initialize theives under MrBigg
    initDetectives()  # initialize Detetives
    weeks = GameParameters().getWeeks()
    weekCounter = 0
    o = open('CrymlandAnalysis.txt', 'w')  # creates output file o
    while(not(cD['MrBiggArrest'])):
        for i in range(weeks):
            t = weekHeist(MrBigg, i, o)  # calls weekheist funciton.
            weekCounter += 1
            if t:
                o.write("Mr Bigg arrested on week: "+str(weekCounter)+"\n")
                o.write("Total Seized Amount: "+str(cD['seizedWealth']))
                break
    o.close()  # close o


main()          #start program 
