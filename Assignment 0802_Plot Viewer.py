# Name: Mark Haskins
# Date: 3/1/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assignment 0802: Plot Viewer
# Link to video: https://youtu.be/YzPyIaR6Z5E

from random import choice, sample
from os import listdir
from os.path import isfile, join, abspath

       
class SimplePlotGenerator():
    '''plot generator class that returns simple plot'''
        
    def getFileData(self):
        '''Function to get data from text files and returns a dictionary containing key, value of file name and text value as a list'''
        ext = ".txt" 
        myDir = "C:\\Users\\mhask\\OneDrive\\Documents\\Academics\\Depaul\\DSC430\\Assignments\\Assignment 0801_Plot Generator\\"
        fPathList = [join(myDir,f) for f in listdir(myDir) if isfile(join(myDir,f)) and f.endswith(ext)]   #listdir returns contents in my diretory
        plotDict = {}                           #checks that directory item is a file(not a folder) and ends with extension .txt
        for fname in fPathList:
            with open(fname) as fn:
                items = [i.strip() for i in fn.readlines()]
            plotDict[fname.replace(myDir, "").replace(ext,"")] = items      
        return plotDict 

    def registerPlotViewer(self, pv):               
        '''function to register plot viewer'''
        self.pv =  v

    def generate(self):
        '''function to return string something happens'''
        return "Something Happens"

class RandomPlotGenerator(SimplePlotGenerator):
    '''random plot generator class'''
    
    def generate(self):
        '''function is overridden to return a plot based upon random choices from text file'''
        d = self.getFileData()
        plot = str(choice(d.get("plot_names"))+", a "+ choice(d.get("plot_adjectives"))+" "+choice(d.get("plot_professions")) +", must "
        + choice(d.get("plot_verbs"))+" the "+ choice(d.get("plot_adjectives_evil")) + " " + choice(d.get("plot_villian_job")) +", " + choice(d.get("plot_villians")))
        return plot

class InteractivePlotGenerator(SimplePlotGenerator):
    '''interactive plot generator class'''

    def generate(self):
        '''function is overridden to return a plot based upon user selected input'''
        self.d = self.getFileData()
        self.nd = self.getNestedDict()
        qL = [
            "Chose a hero's name from the list by typing the corresponding number ",
            "Chose a hero's adjective from the list by typing the corresponding number ",
            "Chose a hero's profession from the list by typing the corresponding number ",
            "Chose a hero's verb from the list by typing the corresponding number ",
            "Chose a villian's adjective from the list by typing the corresponding number ",
            "Chose a villan's job from the list by typing the corresponding number ",
            "Chose a villan's name from the list by typing the corresponding number "
            ]
        l = []
        for q,v in zip(qL,self.nd):     #zip allows iteration through the question list and nd dcitionary at the same time. 
            x = self.pv.queryUser(q + str(self.nd.get(v))+ ": ")
            l.append(int(x))                    #append value entered as an integer and store in list l
        
        plot = str(
        self.nd[1][l[0]]+", a "+                #use of indexes to 
        self.nd[2][l[1]]+" "+
        self.nd[3][l[2]]+", must "+
        self.nd[4][l[3]]+" the "+
        self.nd[5][l[4]]+" "+
        self.nd[6][l[5]]+", "+
        self.nd[7][l[6]]
        )
        return plot
                
    def getSubDict(self,fn):
        '''function to create random subdictionary using 5 random values in parent plot dictionary'''           #create random sub Dictionary
        n,k,self.subD = 5,0,{}      
        x = sample(self.d.get(fn),5)
        for v in x:
            k += 1
            self.subD[k] = v
        return self.subD

    def getNestedDict(self):
        '''function to produce nested dictionary where key is incremented and values are subdictionarys'''
        k,self.nd = 0,{}    #create empty dictionary and set key to 0
        filenames = ["plot_names","plot_adjectives","plot_professions","plot_verbs","plot_adjectives_evil","plot_villian_job","plot_villians"]  
        #retyped file names to get into correct order 
        for fn in filenames:
            v = self.getSubDict(fn) 
            k +=1                           #increment key to act as user input
            self.nd[k] = v
        return self.nd 

class PlotViewer():
    def registerPlotGenerator(self, pg):
        '''function to register a plot generator'''
        self.pg = pg
        self.pg.registerPlotViewer(self)

    def queryUser(self, str):
        '''function to query user and returns input function that accepts a string'''
        return input(str)
    
    def generate(self):
        '''function to print out results of generator function'''
        print(self.pg.generate())
    
def main():
    '''main function to initialze a plot viewer and register three plot generators'''
    pv = PlotViewer()
    pv.registerPlotGenerator( SimplePlotGenerator() )
    pv.generate()
    pv.registerPlotGenerator( RandomPlotGenerator() )
    pv.generate()
    pv.registerPlotGenerator( InteractivePlotGenerator() )
    pv.generate()

main()

