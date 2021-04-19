# Name: Mark Haskins
# Date: 1/25/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assignment 0301_GoldbachConjecture
# Link to youtube video: https://youtu.be/FBNSIZGzg5Y
from math import sqrt, floor

def greetUser():
    '''Function to greet user and explain purporse of the program'''
    print(
        """
    Hello this program will simulate Goldbach's Conjecture that every even integer greater than two can be 
    expressed as the sum of two prime numbers. This program will print out a sinlge line showing two prime 
    numbers added together to equal every even integer in the range 2 to n
    """
    )


def getInput():
    '''
        Function to get user input. Function will throw an exception if non-integer value is entered that cannot
        cannot be parsed or if a value less than 2. Function will loop until input is entered correctly.
    '''
    while True:
        try:
            n = int(input("Please enter an integer greater than 2: "))
        except ValueError:
            print("Input is invalid please try again.")
            continue
        if n <= 3:
            print("Input is not an even integer greater than 2")
        else:
            break
    return n


def isPrime(n):
    '''Function to check whether an integer is prime or not. Returns a boolean value'''
    if n == 1:                              # 1 is not a prime number
        return False
    maxDivisior = floor(sqrt(n))            # improved by reducing number of divisors, because divisors repeat themselves after finding sqrt(n) * sqrt(n), use floor for numbers not in a perfect square. 
    for i in range(2, maxDivisior+1):       # start at 2, since 1 is not prime
        if (n % i == 0):                    # Originally, if original number is divisible by any number in range 2 to that original number then that new number is a factor and original number is not prime
            return False                    # 
    return True


def getPrimes(n):
    '''Function returns a list of prime numbers from 2 to N.'''
    primesList = []                         # empty list to store primes
    for i in range(2, n + 1):
        if isPrime(i):                      # append prime numbers to list after calling isPrime function
            primesList.append(i)
    return primesList


def listEvenNumberN(n):
    '''Function returns a list of even numbers from 2 to N'''
    evenNumList = []                        # empty list to store even numbers
    for i in range(4, n+1):
        if i % 2 == 0:                      # if number is divisible by 2 with no remainer, it is in even number
            evenNumList.append(i)           # append even number to list
    return evenNumList


def sumPair(primesList, evenNumList):
    '''Function takes a list of even numbers and and list of prime numbers to N respectively
        and returns a list of lists of their sum pairs.     
    '''
    sumPairList2D = []                      # empty list
    for evenNum in evenNumList:
        for primeNum in primesList:         #nest for loop to loop through even numbers list and then trhough prime numbers 
            diff = evenNum - primeNum
            if primeNum > diff:             # so sum numbers aren't repeated after the first pair is found, for example 7 = 10 -3
                break                       # if 3 > 7, so continue, but next time 3 = 10 - 7, so 7 > 3, break
            if diff in primesList:          # append list within a list
                sumPairList2D.append([primeNum, diff, evenNum])
    return sumPairList2D                    # returns 2 dimensional list


def displayResult(sumPairList):
    '''Function prints the sum pairs on a single line'''
    print("Results:")
    for row in sumPairList:
        print(f"{row[0]:3}  + {row[1]:3}  = {row[2]:3}")    # f string to print out each row with a pad of 3 spaces on the console


def main():
    '''main function to greet user, get input, and display result'''
    greetUser()
    n = getInput()
    primesList = getPrimes(n)
    evenNumList = listEvenNumberN(n)
    sumPairList2D = sumPair(primesList, evenNumList)
    displayResult(sumPairList2D)


main()
