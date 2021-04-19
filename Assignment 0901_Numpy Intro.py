# Name: Mark Haskins
# Date: 3/8/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assignment 0901: Numpy Intro
# Link to video: https://youtu.be/_ryRocpQxaI 

import numpy as np


def main():
    '''main function to create and display different array functions'''
    a = np.arange(0,100) 
    print("Array a:")
    print(a) 
    print()                                  #use of arrange function to create a 0-99, 100 is not included           .
    b = np.arange(0,100,10)    
    print("Array b:")
    print(b) 
    print()                                 #use of 10 as the step for 10 equally-spaced values          
    c = np.linspace(0,10,100)   
    print("Array c:")
    print(c) 
    print()                                 #because values need to be placed at .1, use 100. There are 10 .1 between each number and there are 10 numbers so 10x10 =100
    d = np.random.random((10,10)) 
    a = np.arange(100).reshape(10,10)
    print("Result of a[4,5]:")          #4,5 can be read the 5th element within the 4th sub array 
    print(a[4,5])
    print()
    print("Result of a[4]:")  
    print(a[4])                         #can be read as the fourth sub array 
    print()
    print("Sum of array d:")
    print(d.sum())
    print()
    print("Max of array a:")
    print(a.max())
    print()
    print("Transpose of array b:")
    print(b.transpose())
    print()
    print("a+d:")
    print(a+d)
    print()
    print("a*d:")                      #a*d multiplication is done element wise 
    print(a*d)
    print()
    print("Dot Product of a and d:")
    print(np.dot(a,b))

main()
