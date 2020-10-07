#Day 14

#Practice problem 1
print('Practice problem 1:\n')

def countOccurrences(bigstr, substr):
    amount = bigstr.count(substr)
    return amount

print('The number of times','"ss" appears in','"Mississippi" is',countOccurrences('Mississippi','ss'))


#Practice problem 2:
print('\nPractice problem 2:\n')

def removeFirst(bigstr,substr):
    location = bigstr.find(substr)
    sublen = len(substr)
    newstring = bigstr[0:location] + bigstr[location+sublen: ]
    #This creates a newstring that is ([start of bigstr -> before the start of substr] + [1 after the end of substr ->  the end of bigstr])
    return newstring


print(removeFirst('A bobcat is a big cat.','cat'))

#Practice problem 3:
print('\nPractice problem 3:\n')

def removeAll(bigstr, substr):
    i = 0
    newstring = ''
    while i < (len(bigstr)):
        if substr == bigstr[i:i+len(substr)]:
            newstring += ''                     #This is just for my brain to understand; add nothing to the newstring
            i+=len(substr)
        else:
            newstring += bigstr[i:i+1]          #Add the current character to newstring
            i+=1
            
    return newstring


print(removeAll('A bobcat is a big cat.','cat'))
