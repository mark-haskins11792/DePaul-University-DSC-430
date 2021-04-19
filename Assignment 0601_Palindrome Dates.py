# Name: Mark Haskins
# Date: 2/15/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assingmentt 0601: Palindrome Dates
# Video Link: https://www.youtube.com/watch?v=82erVC4E1YI&feature=youtu.be


def getPalindromedates(strDate, endDate): 
    '''returns list of all palindrome dates between given start and end dates'''
    palindromeList = []
    strYear, endYear =  strDate[-4:], endDate[-4:]
    for year in range(int(strYear),int(endYear)+1,1):
        strYear = str(year)
        revStrYear = strYear[::-1]          #reverse year 
        day = int(revStrYear[0 : 2])        #day digits has to be inside year digits 
        month = int(revStrYear[2 : 4])      #month digits has to be inside year digits
        revStrYear += strYear               
        if validDayMonth(day, month):
            palindromeList.append(revStrYear)
    return palindromeList


def validDayMonth(day, month):
    '''function to check whether day and month are a valid combination'''
    month30days = (4,6,9,11)                    #Apr,Jun,Sep, Nov have 30 days
    if (day < 1 or day > 31):
        return False
    if (month < 1 or month > 12):
        return False
    if day > 30 and month in month30days:
        return False
    if day > 28 and month is 2:                 #Feb has 28 days
        return False
    return True
    

def output(palindromeList):
    '''function to output palindrome dates into a text file'''
    outfile = open('palindromedates.txt', 'w') #creates and outputs a file 
    for palindrome in palindromeList:
        outfile.write(f"{palindrome[0:2]}/{palindrome[2:4]}/{palindrome[-4:]}\n")
    outfile.close()

def main():
    '''main method to run program'''
    palindromeList = getPalindromedates("01012001", "31122100")  #start and end dates of 21st century 
    output(palindromeList)
 
main()



