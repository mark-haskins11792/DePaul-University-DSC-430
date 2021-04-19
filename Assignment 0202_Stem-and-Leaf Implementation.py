# Name: Mark Haskins
# Date: 1/18/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assignment 0202_Stem-and-Leaf Implementation

def getFileData(num):
    '''
    Function receives integer and reads in corresponding text file. 
    Function will return list of sorted integeers from the text file. 
    '''
    fileNameDict = {1: "StemAndLeaf1.txt",
                    2: "StemAndLeaf2.txt", 3: "StemAndLeaf3.txt"}  # stores file name as a dictionary
    # uses raw input string to handle \ as a file directory instead of escape character
    folderPath = r"C:\Users\mhask\OneDrive\Documents\Academics\Depaul\DSC430\Assignments\Assignment 0202_Stem-and-Leaf Implementation"'\\'
    # concats file name in dictionary with file name in
    fileName = folderPath + fileNameDict.get(num)
    # opens file with read only priviledges
    infile = open(fileName, "r")
    lineList = infile.readlines()          # returns list reading each line in file
    infile.close()                         # closes the file
    numbers = []                           # creates empty numbers list
    for i in lineList:                     # iterates through each line in text file and appends number to list, also strips newline character \n
        numbers.append(i.strip())
    numbersList = list(map(int, numbers))  # converts string list to integers
    # sorts the numbers list in order to order leaves correctly
    numbersList.sort()
    return numbersList                     # returns list of integer numbers


def getInput():
    '''
    Function prompts user for input  and returns valid integer 1, 2 or 3 if selected
    Function will throw an exception if non-integer value is inputed and ask user to try again. 
    '''
    while True:
        try:
            # requests user input
            num = int(input("Please enter a 1, 2, or 3 to select file number: "))
            if num == 1 or num == 2 or num == 3:
                return num
            else:
                # handles integers other than 1,2,3
                print("Input is invalid. Please try again.")
                continue
        except ValueError:  # handles non-integer values including strings
            print("Input is invalid. Please try again.")


def greetUser():
    '''Function to greet user and explain the program'''
    print("Hello, this program generates a stem and leaf plot based upon one of three file types selected.")


def exitFunction():
    '''
    Function prompts user to type E or C to exit or continue. Based upon input received
    Function will return True, False or prompt user to provide valid input. 
    '''
    while True:
        choice = input(
            "Please type 'E' to exit the program or 'C' to continue: ")
        if choice == "E":
            print("Exiting the program")
            return True
        elif choice == "C":
            print("Continuing the program")
            return False
        else:
            print("Input is not valid. Please try again.")
            continue


def displayStemLeaf(slDict):
    '''
    Fuction receives a dictionary as an arugment and prints the key value pairs
    as a stem and leaf plot. 
    '''
    for s, l in slDict.items():  # s,l stand for key value pairs stem and leaves in the slDict
        print(s, end="|")  # first for loop prints stem with pipe delimiter
        for i in l:  # nested for loop prints all the leaves and a single space for each stem.
            print(i, end=' ')
        print()  # prints new line for each stem


def getStemLeaf(num):
    '''
    function receives integer number and returns two corresponding
    integers 's' as stem and 'l' as leaf.  
    '''
    s = num // 10                       # floor division returns each stem using base 10
    # modular division returns remainder as a leaf using base 10
    l = num % 10
    return s, l


def createStemLeafDict(numbersList):
    '''
    function receives numberslist and returns a dictionary containing
    a stem for the key and a list of leaves for the corresponding value
     '''
    slDict = {}  # create empty dictionary
    for i in numbersList:  # iterate through each number in list
        s, l = getStemLeaf(i)  # return each integer as stem and leave
        # store stem as key and leave as empty list. if key is not found, creates a new corresponding empty list and appends the first stem.
        slDict.setdefault(s, []).append(l)
    return(slDict)


def main():
    '''
    Main function to great user and display stem and leaf plot based upon selected file with integer data 
    Program will continue to loop until user decides to exit
    '''
    greetUser()
    exit = False
    while exit == False:
        num = getInput()
        numbersList = getFileData(num)
        slDict = createStemLeafDict(numbersList)
        displayStemLeaf(slDict)
        exit = exitFunction()


main()
