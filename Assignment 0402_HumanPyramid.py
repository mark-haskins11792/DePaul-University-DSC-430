# Name: Mark Haskins
# Date: 2/1/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assignment 0402_HumanPyramid
# Link to youtube video: https://youtu.be/0NgWbiCtQLY 


def humanPyramid(row, column):
    ''' Recursive function to return integer weight stacked ontop of any 
        1 individual human pyramid 
    '''
    if row == 0 and column == 0:                                         #base case, if row = 0 and column = 0 then at top of pyramid and no t 
        return 0
    elif column < 0 or column > row:                                     #base case, if column is less than 0 or column greater than the current row, than off the edge  
        return 0
    else:
        if column == 0 or column == row:
            return 128/2 + (humanPyramid(row-1,column-1) + humanPyramid(row-1,column))/ 2      #edge case only takes half the weight
        else:
            return 128 + (humanPyramid(row-1,column-1) + humanPyramid(row-1,column))/ 2        #case for full weight


def getIput():
    '''Function gets two integer values from user for row and column index'''
    row = int(input("Please input an integer for a row number between 0 and 4: "))
    column = int(input("Please input an integer for a column number between 0 and 4: "))
    return row, column

def displayResult(row,column,weight):
    '''Function displays the result'''
    print(f"Person at ({row}),({column}) has a combined weight on their back of {weight} pounds.")

def main():
    '''Main function to run program, get input, calculate the value, and display the result.'''
    row, column = getIput()
    weight = humanPyramid(row,column)
    displayResult(row,column,weight)
    print("End of main function")

main()
