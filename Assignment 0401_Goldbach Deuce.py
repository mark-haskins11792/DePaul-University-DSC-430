# Name: Mark Haskins
# Date: 2/1/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assignment 0401_Goldbach Deuce
# Link to youtube video: https://www.youtube.com/watch?v=YuKIiv5jWRk 

from random import randint


def greetUser():
    '''Function to greet user and explain purporse of the program'''

    print(
        '''
        This program will generate a random list of integers between 0 and 100. The length of this list will be designated by the user. 
        The program will then prompt the user for a target sum value. If any two of the randomly generated numbers' sum equals
        the target sum value entered by the user, the program will find the first of those two numbers if they exist.  
        '''
    )


def getInput():
    '''
        Function to get user input. Function will throw an exception if non-integer value is entered that cannot
        cannot be parsed or if a value not in range 0 to 100. Function will loop until input is entered correctly.
    '''
    while True:
        try:
            l = int(input("Please enter length as a postivie integer: "))
        except ValueError:
            print("Input is invalid please try again.")
            continue
        if l < 0:
            print("Input is not a positive")
            continue
        else:
            break
    while True:
        try:
            s = int(input("Please enter a target sum as a a postive integer: "))
        except ValueError:
            print("Input is invalid please try again.")
            continue
        if s < 0:
            print("Input is not a positive integer")
            continue
        else:
            break
    return l, s


def sortedRandomList(l):
    '''Function returns a sort list of integers size L.'''
    sRandList = []
    for i in range(0, l):
        n = randint(0, 100)     #use of random integers 1 through 100
        sRandList.append(n)
    sRandList.sort()            #use of pythongs built in sort
    return sRandList


def findSumPair(x, sRandList):
    '''
    Function to find a sum pair based upon inputted random list and target value.
    If pair exists, function returns the two numbers and the sum. If pair does not exist function
    returns to None types and the sum
    '''
    for i in range(len(sRandList)):  # outer loop in n time
        diff = x - sRandList[i]
        if (diff == sRandList[i]):
                                     # if difference is in the list, conditional checks if the next element is equal to current element.
            if sRandList[i] == sRandList[i+1]:
                return(sRandList[i], sRandList[i+1], x)  # returns 0.
            else:
                return None, None, x
        if(search(diff, sRandList)):  # calls binary search
            return sRandList[i], diff, x
        else:                         # if search returns false
                                      # returns None,None,X to calling function to pass these variables to displaySumResult funciton.
            return None, None, x


def search(diff, sRandList):
    '''function executes a binary search algorithmn'''
    low = 0
    high = len(sRandList) - 1
    while low <= high:               # binary search in log(n) time
        mid = (low + high)//2        # Position of middle item
        item = sRandList[mid]
        if diff == item:             # if difference is in the list, returns True
            return True
        elif diff < item:            # x is in lower half of range
            high = mid - 1           # move top marker down
        else:                        # x is in upper half of range
            low = mid + 1            # move bottom marker up
    return False


def displaySumResult(num1, num2, x, sRandList):
    '''Function to display output to console'''
    print(f"For random(sorted) list:\n{sRandList}")
    if num1 == None and num2 == None:
        print(f"There are no two numbers that equal {x}.")
    else:
        print(f"{num1} and {num2} equal target sum {x}.")


def main():
    '''main function to greet user, get input, and display the two numbers that equal the targe value.'''
    greetUser()
    l, s = getInput()
    sRandList = sortedRandomList(l)
    num1, num2, x = findSumPair(s, sRandList)
    displaySumResult(num1, num2, x, sRandList)


main()
