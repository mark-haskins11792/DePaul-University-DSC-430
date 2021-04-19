# Name: Mark Haskins
# Date: 1/25/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assignment 0302_HappyPrimes
# Link to youtube video: https://youtu.be/pGhO-I6WdHE

def getInput():
    '''
    Function to get user input. Function will loop until valid
    input is provided. Function returns an integer value. 
    '''
    while True:
        try:
            n = int(input("Please enter a positive integer: "))
        except ValueError:
            print("Input is invalid please try again.")
            continue
        if n < 0:
            print("Input is not a postive integer. Please try again.")
        else:
            break
    return n


def isPrime(n):
    '''Function to check whether an integer is prime or not. Returns a boolean value'''
    if n == 1:                  # 1 is not a prime number
        return False
    for i in range(2, n):       # start at 2, since 1 is not prime
        if (n % i == 0):        # if original number is divisible by any number in range 2 to that original number then that new number is a factor and original number is not prime
            return False
    return True


def sumSquaredDigits(n):
    '''Function to replace number by sum of the squares of it's digits. Returns an integer value'''
    number = str(n)             # convert n to a string to iterate throught it
    sum = 0
    for digit in number:        # each digit is an element in number string            
        sum += int(digit)**2    # for each digit, caste it back to an integer, square it and increment the sum. Loop through next digit
    return sum


def isHappy(n):
    '''Function to determine whether a number is happy or not. Returns a boolean value'''
    emptyList = []                  # empty list to store previous values
    while True:
        temp = sumSquaredDigits(n)  # set temp variable to sumSquared Digits
        if temp == 1:               # if equals 1 then happy per description
            return True
        elif temp in emptyList:     # if already in empty list, than sum of a squared digits will repeat itself and endlessly loop, so it's sad
            return False
        else:
                                    # if not 1 or sad, repeat the process by storing the vavlue in the empty list
            emptyList.append(temp)
            n = temp                # set n to temp value and pass it through sumSquardedFunction again to iterate until the next 1 of three scenrios happen


def outputStatus(n):
    '''Function to display status of number to console'''
    if isPrime(n):
        if isHappy(n):
            print(f"{n} is a happy prime")
        else:
            print(f"{n} is a sad prime")
    else:
        if isHappy(n):
            print(f"{n} is a happy non-prime")
        else:
            print(f"{n} is a sad non-prime")


def main():
    '''Function is main method to run program. Prompts user for integer and output's the status of the number'''
    while True:  # endless loop that requests and accepts an integer from a user
        n = getInput()
        outputStatus(n)


main()
