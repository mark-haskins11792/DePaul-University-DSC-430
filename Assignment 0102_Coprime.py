# Name: Mark Haskins
# Date: 1/11/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assignment 0102: Coprime

def coprime(a, b):
    '''fuction takes two numbers and returns the highest common factor using Euclidean algorithm'''
    # source: https://sites.math.rutgers.edu/~greenfie/gs2004/euclid.html
    while b != 0:  # while loop - b not equal to zero, as zero for b means the remainder of a mod b = 0 meaning the final b must diivide the final a
        a, b = b, a % b  # swap a with b and b with a mod b
    return a


def coprime_test_loop():
    '''function takes no arguments and prommpts user two enter two integer values or press 0 to to exit the program. 
    Once two values are entered it determines whether or not the two numbers are coprime and returrns the highest common factor'''
    while True:
        num1 = int(input("Please enter an integer or 0 to exit: "))
        if num1 == 0:
            print("Exit")
            break
        num2 = int(input("Please enter a second integer or 0 to exit: "))
        if num2 == 0:
            print("Exit")
            break
        result = coprime(num1, num2)  # calls function using input of
        if result == 1:
            print("Numbers are coprime. Highest common factor is 1")
        else:
            print("Numbers are not coprime. Highest common factor is " + str(result))


coprime_test_loop()
