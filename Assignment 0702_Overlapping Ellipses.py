# Name: Mark Haskins
# Date: 2/22/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assignment 0702: Overlapping Ellipses
# Link to video: https://youtu.be/xjVE_PmdozA

import math
from statistics import mean
import os


class WarAndPeacePseudoRandomNumberGenerator():
    '''Class the represents a pseudo random number generator based upon war and peace text file'''

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
            # seek function only supported in binary mode
            self.fp = open(self.f, "rb")
        except OSError as exception:
            print(exception)

    def getFileSize(self):
        '''method to return file size as an integer value'''
        self.fsize = int(os.path.getsize(self.f))
        return self.fsize

    def setSeedPosition(self):
        '''method to set seed position'''
        self.seedPosition = self.fp.seek(self.sn, 1)
        return self.seedPosition

    def getNextChar(self):
        '''recursive method to get next character'''
        if self.getCursorPosition() < self.getFileSize():
            self.nextPos = self.fp.seek(99, 1)  # move 99 characters
            self.nextChar = self.fp.read(1)
        else:
            self.setCursorPositionBeginning()
            self.getNextChar()
        # convert back to string, so I can read it
        return str(self.nextChar, encoding='ascii', errors='replace')

    def getCharList(self):
        '''method to return converted character list'''
        self.charList = []  # stop exclusive, need 33
        for char in range(32):
            self.a = self.getNextChar()
            self.b = self.getNextChar()
            while self.b == self.a:
                self.b = self.getNextChar()
            else:
                self.charList.append([self.a, self.b])
        return self.charList

    def getByteList(self):
        '''method to return a byte list'''
        self.bytesList = []
        for row in self.charList:
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
            self.numList.append(b/2**self.x)
            self.x += 1
        self.num = sum(self.numList)
        return self.num

    def getCursorPosition(self):
        '''method to get current cursor position'''
        currentCursorPosition = self.fp.tell()
        return currentCursorPosition

    def setCursorPositionBeginning(self):
        '''random method to return a single random number'''
        self.fp.seek(0)

    def random(self):
        '''method to retrun a list of 10,000 random numbers. Takes an object as a parameter'''
        self.getCharList()
        self.getByteList()
        self.randomNum()
        return self.num


class Point:
    '''represents a coordinate point in x,y format'''
    def __init__(self, xcoord=0, ycoord=0):
        '''method to intialize a point, takes an x and y coordinate, defaults to zero if none are given'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        '''set x coordinate'''
        self.x = xcoord

    def sety(self, ycoord):
        '''set y coordinate'''
        self.y = ycoord

    def get(self):
        '''return x and y coordinates as integers'''
        return (self.x, self.y)

    def getX(self):
        '''return x coordinate as integer'''
        return self.x

    def getY(self):
        '''return y coordinate as integer'''
        return (self.y)

    def move(self, dx, dy):
        '''shift x and y coordinates by integer parameters provided'''
        self.x += dx
        self.y += dy

    def displayPoint(self):
        self.xp = self.getX()
        self.yp = self.getY()
        print(f"Point:({self.xp},{self.yp})")

class Ellipse():
    '''represents an elipse'''

    def __init__(self, focalPoint1, focalPoint2, width):
        '''initialises ellipse with two focal points and width'''
        self.f1 = focalPoint1
        self.f2 = focalPoint2
        self.w = width

    def inEllipse(self, point):
        '''function to determine if point is within an elipse area'''
        dist = self.pointDistanceFoci(point)
        if dist < self.w:
            return True
        else:
            return False

    def pointDistanceFoci(self, point):
        '''function returns total distance between given point and the ellipse foci'''
        self.p = point
        self.x2, self.y2 = self.f2.get()
        self.x1, self.y1 = self.f1.get()
        self.pX, self.pY = self.p.get()
        self.dist1 = math.sqrt((self.pX - self.x1)**2 + (self.pY - self.y1)**2)     #point distance formula
        self.dist2 = math.sqrt((self.pX - self.x2)**2 + (self.pY - self.y2)**2)
        self.totalDist = self.dist1 + self.dist2
        return self.totalDist

    def getXValues(self):
        '''return x values of foci'''
        return self.f1.getX(), self.f2.getX()

    def getYValues(self):
        '''return y values of foci'''
        return self.f1.getY(), self.f2.getY()

    def getW(self):
        '''return width of ellipse'''
        return self.w


class OverLapEllipse():
    '''class represents two overlapping ellipses'''

    def __init__(self, e1, e2):
        '''function to intialize the point, takes two ellipses as parameters'''
        self.ellipse1 = e1
        self.ellipse2 = e2

    def getBoundary(self):
        '''function return boundaries of box around ellipse as four integer values'''
        self.minX = min(min(self.ellipse1.getXValues(),
                            self.ellipse2.getXValues()))
        self.maxX = max(max(self.ellipse1.getXValues(),
                            self.ellipse2.getXValues()))
        self.minY = min(min(self.ellipse1.getYValues(),
                            self.ellipse2.getYValues()))
        self.maxY = max(max(self.ellipse1.getYValues(),
                            self.ellipse2.getYValues()))
        self.maxW = (max(self.ellipse1.getW(), self.ellipse2.getW()))*.5            #formula provided during lecture 
        self.l = self.minX - self.maxW
        self.r = self.maxX + self.maxW
        self.b = self.minY - self.maxW
        self.t = self.maxY + self.maxW
        return self.l, self.r, self.b, self.t

    def getArea(self):
        '''functin returns total area of boundary box'''
        self.area = (self.t-self.b)*(self.r-self.l)
        return self.area

    def estimateOverLap(self):
        '''function to estimate overlap of the two ellipses'''
        self.numPoints = 2000
        self.insideCount = 0
        self.prng = WarAndPeacePseudoRandomNumberGenerator()            #initialize prng from previous assingment 
        self.count = 0
        for i in range(self.numPoints):
            self.count += 1
            rP = self.getRandomPoint()                                  #generates random point 
            if self.ellipse1.inEllipse(rP) and self.ellipse2.inEllipse(rP): #checks to see if random points lies within both ellipses 
                self.insideCount += 1               
        self.overlap = self.insideCount/self.numPoints*self.area       #returns overlap as a float
        return self.overlap

    def scale(self, x, y):
        '''function returns to x an y values that are scaled to match boundary'''
        self.sx, self.sy = x, y
        self.sx = (self.l-self.r)*x + self.r
        self.sy = (self.t-self.b)*y + self.b
        return self.sx, self.sy

    def getRandomPoint(self):
        '''function returns a random point in x,y format using W&P PRNG'''
        self.x = self.prng.random()
        self.y = self.prng.random()
        self.sx, self.sy = self.scale(self.x, self.y)
        self.randomPoint = Point(self.sx, self.sy)
        return self.randomPoint
    
    def overLap(self):
        '''function to compute over lap and display the results'''
        self.getBoundary()
        self.getArea()
        self.estimateOverLap()
        self.displayResults()
        

    def displayResults(self):
        '''function to display results'''
        print("Ellipse 1")
        print("Foci 1:")
        self.ellipse1.f1.displayPoint()
        print("Foci 2:")
        self.ellipse1.f2.displayPoint()
        print("Width:")
        print(self.ellipse1.w)
        
        print()
        print("Ellipse 2")
        print("Foci 1:")
        self.ellipse2.f1.displayPoint()
        print("Foci 2:")
        self.ellipse2.f2.displayPoint()
        print("Width:")
        print(self.ellipse2.w)
        print()
        print("Boundaries l,r,b,t:")
        print(self.l, self.r, self.b, self.t)
        print("Total Boundary Area:")
        print(self.area)
        print("Estimated Over Lap:")
        print(self.overlap)


def main():
    p1 = Point(0, 0)
    p2 = Point(0, 0)
    p3 = Point(0, 0)
    p4 = Point(0, 0)
    e1 = Ellipse(p1, p2, 2)
    e2 = Ellipse(p3, p4, 2)
    oE1 = OverLapEllipse(e1, e2)
    oE1.overLap()
    p5 = Point(-1, 1)
    p6 = Point(-1, -1)
    p7 = Point(1, 1)
    p8 = Point(-3, -2)
    e3 = Ellipse(p5, p6, 4)
    e4 = Ellipse(p7, p8, 8)
    oE2 = OverLapEllipse(e3, e4)
    oE2.overLap()

main()
