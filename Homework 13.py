#Ethan Brinkman
#Homework 13: 1, 2, 3
#Due 4/5/2019


#Number 1
print('Number 1\n')

stData = open('studentdata.txt','r')

for line in stData:
    lineList = line.split()
    if (len(lineList) > 7):                 #The 7 is to incorporate the length of the name
        print(lineList[0],'has more than six test scores')
    
stData.close()

#Number 2
print('\nNumber 2\n')

movDat = open('movie_data.txt','r')
outFile = open('billions.txt', 'w')

for line in movDat:
    lineList = line.split('\t')
    if int(lineList[2]) > 1000000000:       #If the movie has grossed over $1B, add it to the file 
        outFile.write(line)

movDat.close()
outFile.close()


#Number 3
print('\nNumber 3\n')

def readWords(fileName):
    file = open(fileName,'r')
    
    unique = []                             #Empty list to place unique strings
    for line in file:
        splitLine = line.split()
        for item in splitLine:
            if item.lower() in unique:      #If the lowercase version is in the list of unique strings
                pass
            else:                           #If the lowercase version isn't in the list of unique strings
                unique.append(item.lower()) #Add a lowercase version of it, as per instructions

    file.close()
    return unique

print(readWords('pat_sat.txt'), 'are all unique strings in pat_sat.txt')
