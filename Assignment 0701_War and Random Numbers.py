# Name: Mark Haskins
# Date: 2/22/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assignment 0701: War and Random Numbers
# Link to video: https://www.youtube.com/watch?v=rliRuPfsTAQ&feature=youtu.be

from statistics import mean 
import os

class WarAndPeacePseudoRandomNumberGenerator():
    

    def __init__(self, seedNum=0):
        '''initilize War and Peace PRNG. Initializing opens the W&P text file. Optional parameter to set the seed number. Default seed number is 0'''
        self.sn = seedNum
        self.openFile()
        self.setSeedPosition()
    
    def openFile(self):
        '''open W&P text file in read + binary mode'''
        self.folderPath = r"C:\Users\mhask\OneDrive\Documents\Academics\Depaul\DSC430\Assignments\Assignment 0701_War and Random Numbers"'\\'
        self.fileName = "war-and-peace.txt"
        self.f = self.folderPath + self.fileName
        try:
            self.fp = open(self.f, "rb")        #seek function only supported in binary mode
        except OSError as exception:            #cathches any OS error exceptions
            print(exception)
    
    def getFileSize(self):
        '''method to return file size as an integer value'''
        self.fsize = int(os.path.getsize(self.f))           #use os class's get size function
        return self.fsize
    
    def setSeedPosition(self):
        '''method to set seed position'''
        self.seedPosition = self.fp.seek(self.sn,1) 
        return self.seedPosition

    def getNextChar(self):
        '''recursive method to get next character'''
        if self.getCursorPosition() < self.getFileSize():       #base case to get whether current cursor postion is less than file size
            self.nextPos = self.fp.seek(99,1)                   #set step to 99 characters per requirement
            self.nextChar = self.fp.read(1)
        else: 
            self.setCursorPositionBeginning()                  #if cursor position = current file size, set cursor position to beginning
            self.getNextChar()                                 #recursive function
        return str(self.nextChar,encoding= 'ascii',errors='replace')     #convert bytes to string using ascii format (default is UTF-8), replaces errors with a ?                    
    
    def getCharList(self):
        '''method to return converted character list'''
        self.charList = []                               #stop exclusive, need 33 
        for char in range(32):
            self.a = self.getNextChar()
            self.b = self.getNextChar()
            while self.b == self.a:                     #method to test if current character is equal to next character, if yes then get another character  
                self.b = self.getNextChar()
            else:
                self.charList.append([self.a,self.b])   #method will return a list of two elements (characters) with a list
        return self.charList   
    
    def getByteList(self):
        '''method to return a byte list'''
        self.bytesList = []
        for row in self.charList:                   #method evaluates each element in each 2 element list and returns a 1 or 0 based upon ascii number size. 
            if row[0] > row[1]:
                self.bytesList.append(1)
            else:
                self.bytesList.append(0)
        return self.bytesList
    
    def randomNum(self):
        '''method to return a single number from bytesList'''
        self.numList = []
        self.x = 1
        for b in self.bytesList:
            self.numList.append(b/2**self.x)        #use of formula provided, each byte is halfed and then raised to incrementing power 0.5,0.25,0.125 etc 
            self.x += 1                              #increment the power
        self.num = sum(self.numList)                #sum the list to return single random number value
        return self.num

    def getCursorPosition(self):
        '''method to get current cursor position'''                    
        currentCursorPosition = self.fp.tell()
        return currentCursorPosition

    def setCursorPositionBeginning(self):
        '''method to set cursor position to the beginning of the file'''
        self.fp.seek(0)
    
    def random(self):  
        '''random method to return a single random number'''             
        self.getCharList()
        self.getByteList()
        self.randomNum()
        return self.num        
    
def randomNumList(obj):
    '''method to retrun a list of 10,000 random numbers. Takes an object as a parameter'''
    randomNumList = []
    for i in range(10000):
        randomNumList.append(obj.random())
    rnl = randomNumList
    return rnl

def displayResults(rnl):
    '''method to display results of random number list's length, average, max, min along
    with first 10 random numbers in the list'''
    rnlLength = len(rnl)
    rnlMean = mean(rnl)
    rnlMax = max(rnl)
    rnlMin = min(rnl)
    print(f"Random Number List Length: {rnlLength}")
    print(f"Random Number Average: {rnlMean}")
    print(f"Random Number Max: {rnlMax}")
    print(f"Random Number Min: {rnlMin}")
    print(f"First 10 random numbers in the list: ")
    for num in range(10):           #set range to 10 so numbers could be seen clearly in console 
        print(rnl[num])
     

def main():
    '''method to initialize W&P generator and display results'''
    prng = WarAndPeacePseudoRandomNumberGenerator(12345)
    rnl = randomNumList(prng)
    displayResults(rnl)

main()
