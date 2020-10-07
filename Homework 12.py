#Ethan Brinkman
#Homework 12: 2 - 12 even
#Due 4/3/2019

import random

#====================Functions to call====================

#Number 4 function:
def average(nL):
    runTot = 0
    for item in nL:
        runTot += item
        
    result = runTot // len(nL)
    return result

#Number 6 function:
def sum_of_squares(xs):
    sumTot = 0
    for item in xs:
        sumTot += item**2
        
    return sumTot

#Number 8 function:
def evenSum(nL):
    runTot = 0
    for item in nL:
        if item % 2 == 0:
            runTot += item
        else:
            pass
        
    return runTot

#Number 10 function:
def isLenFive(l):
    count = 0
    for item in l:
        if len(item) == 5:
            count += 1
        else:
            pass
        
    return count

#Number 12 function:
def throughSam(l):
    count = 0
    for item in l:
        if item != 'Sam':
            count += 1
        else:  
            return count + 1
        

#====================Main() and num. 2====================

def main():
    
    #Number 2:
    print('Number 2:\n')

    referenceList = [76, 92.3, 'hello', True, 4, 76]
    mylistConc = []
    mylistApp = []

    for item in referenceList:
        mylistConc += [item]
        pass

    for item in referenceList:
        mylistApp.append(item)
        
    print(mylistConc, 'is the list created with concatenation, and', mylistApp, 'is the list created through appending.')

    #Number 4:
    print('\nNumber 4:\n')

    numList = []
    for i in range(100):
        numList.append(random.randrange(1,1001))    #Making the list of 100 numbers from 1 through 1000
        
    print(average(numList))


    #Number 6:
    print('\nNumber 6:\n')
    
    numList = input('Type in however many integers you want, separate each integer with a space\n')
    numList = numList.split(' ')
    numList = [int(item) for item in numList]       #Changing each variable in the list to an integer class               

    print('The sum of squares for this number list is', sum_of_squares(numList))

    #Number 8:
    print('\nNumber 8:\n')

    print('Using the number list you entered in the previous problem and adding only the even numbers we get a result of', evenSum(numList))

    #Number 10:
    print('\nNumber 10:\n')

    strList = input('Type in a string of words, and I will tell you how many words are 5 characters long\n')
    strList = strList.split(' ')
    print('The number of 5-character-long words in that string is', isLenFive(strList))

    #Number 12:
    print('\nNumber 12:\n')

    nameList = ['Alex', 'Johnathan', 'Merle', 'Marilyn', 'Benjamin', 'Sam', 'Chad', 'Ethan', 'Rebecca']
    print('I have a list of names here.\nThey read:',nameList)
    print('The number of names up to and including "Sam" that occur is', throughSam(nameList))
    
main()
