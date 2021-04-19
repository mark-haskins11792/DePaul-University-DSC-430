# Name: Mark Haskins
# Date: 1/11/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assignment 0101_Grading Logic
# Link to youtube video: https://youtu.be/6cfc42_iXgE

def correct_file():
    '''function prompts user for Y/N if assignment is submitted in the correct file and returns a boolean'''
    fileIncluded = input(
        "Is the assignment submitted as a single uncompressed .py file? Type(Y/N): ")
    if fileIncluded == 'Y':  # helper fuction using if logic and returning a boolean
        return True
    if fileIncluded == 'N':
        return False


def includes_name():
    '''function prompts user for Y/N if name is entered and returns a boolean'''
    name = input("Did the student enter their name? Type(Y/N): ")
    if name == 'Y':
        return True
    if name == 'N':
        return False


def includes_date():
    '''function prompts user for Y/N if date is entered and returns a boolean'''
    date = input("Did the student include the date? Type(Y/N): ")
    if date == 'Y':
        return True
    if date == 'N':
        return False


def includes_honor_statement():
    '''function prompts user for Y/N if honor statement is entered and returns a boolean'''
    honor = input("Did the student include the honor statement? Type(Y/N): ")
    if honor == 'Y':
        return True
    if honor == 'N':
        return False


def includes_video():
    '''function prompts user for Y/N if youtube video is included and returns a boolean'''
    video = input(
        "Does the assignment inlcude an unlisted 3-minute Youtube video? Type(Y/N): ")
    if video == 'Y':
        return True
    if video == 'N':
        return False


def code_correctness():
    '''function prompts user to enter numeric value between 1 and 10 and returns an int'''
    points = int(input(
        "Out of ten points, how would you evaluate the code correctness? Type(1..10): "))   # casting string input as an intger to return integer for points
    return points


def code_elegance():
    '''function prompts user to enter numeric value between 1 and 10 and returns an int'''
    points = int(input(
        "Out of ten points, how would you evaluate the code elegance? Type(1..10): "))
    return points


def code_hygiene():
    '''function prompts user to enter numeric value between 1 and 10 and returns an int'''
    points = int(input(
        "Out of ten points, how would you evaluate the code hygiene? Type(1..10): "))
    return points


def video_discussion():
    '''function prompts user to enter numeric value between 1 and 10 and returns an int'''
    points = int(input(
        "Out of ten points, how would you evaluate the video discussion? Type(1..10): "))
    return points


def hours_late():
    '''function prompts user to enter an integer value for hours late and returns a float'''
    hours = int(input(
        "How many hours late was the assignment? If not late, type 0 else type a whole number: "))
    if hours == 0:
        return 0
    # using .4 literal to compute how late the assignment was
    return float(hours * .4)


def compute_grade():
    '''computes grade for class'''
    if not(includes_name()):  # calling previously defined helper functions
        # if return boolean is not true (false) then sets local grade variable to zero
        grade = 0
        print("Grade: " + str(grade))  # converts int grade value to string so it can't print to console
        return 0  # return zero to show succesfully exit of them
    if not(includes_date()):
        grade=0
        print("Grade: " + str(grade))
        return 0
    if not(includes_video()):
        grade=0
        print("Grade: " + str(grade))
        return 0
    if not(includes_honor_statement()):
        grade=0
        print("Grade: " + str(grade))
        return 0
    if not(correct_file()):
        grade=0
        print("Grade: " + str(grade))
        return 0
    # calling each helper function and storing points in the result
    result1=code_correctness()
    result2=code_elegance()
    result3=code_hygiene()
    result4=video_discussion()
    result5=hours_late()
    # final grade variable is a sum of first 4 results - the fifth results for hours late.
    grade=(result1 + result2 + result3 + result4) - result5
    print(grade)  # prints final grade to the console
    return grade

compute_grade()  # calling compute_grade function to start the program.
