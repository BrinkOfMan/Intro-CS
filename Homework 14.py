#Ethan Brinkman
#Homework 14: Number 1 and 2
#Due 4/8/2019

#Number 1
print('Number 1:\n')

def countAlpha(astr):
    counts = {}
    for char in astr:
        if char.isalpha():
            if char.lower() in counts:
                counts[char.lower()] += 1
            else:
                counts[char.lower()] = 1
            
    return counts

str1 = input('Please enter a word or short phrase: ')
str2 = input('Now, enter a second word.\nI will see if they are anagrams: ')
counts1 = countAlpha(str1)
counts2 = countAlpha(str2)

print('\nOh, mighty computer, are these two strings anagrams?')
print('[Computer]:',counts1 == counts2)

#Number 2
print('\nNumber 2:\n\nCheck for a word_counts.txt file.') 


milton = open('milton.txt', 'r')
wordCounts = open('word_counts.txt', 'w')
counts = {}

miltonStr = milton.read()                   #Reads in the entirety of milton.txt into this string
miltonStr = miltonStr.lower()               #Also, make it all lowercase for easier reading and compression of lines
splitStr = miltonStr.split()    


#This next chunk took me three hours to write and debug.
#It checks every word, and removes specific instances of non-alpha strings.
idx = ''
for idx in range(len(splitStr)-1):
    Continue = True
    alphaStr = True
    char = 0     
    while Continue:
        if splitStr[idx][char].isalpha():       #Check if that character is alpha
            if char < len(splitStr[idx])-1:
                char += 1
            else:
                Continue = False
                
        elif len(splitStr[idx]) == 1:           #If not alphanumberic, check if it's just a punctutation / otherwise
            splitStr[idx] = 'Removed'
            Continue = False
            
        elif char == len(splitStr[idx])-1:      #If it's the last letter, count it as a complete word
            splitStr[idx] = splitStr[idx][0:char]   #Change it so that only tha alpha bits are included
            Continue = False
            
        elif char == 0 and splitStr[idx][char+1].isalpha():    #If it's just the first character (ex: 'twixt) that's not alpha, check the next
            splitStr[idx] = splitStr[idx][char+1:]
            char += 1

        elif splitStr[idx][char+1].isalpha():       #If there's punctuation in the middle, it's still a word (o'rewhelm'd)
            char+= 1                                
            
        else:
            splitStr[idx] = 'Removed'
            Continue = False

#Count all the words (except instances of 'Removed')
counts = {}
splitStr.sort()
for idx in splitStr:       
    if idx in counts and idx != 'Removed':
        counts[idx] += 1
    else:
        if idx != 'Removed':
            counts[idx] = 1

#Get it into a text file
for item in counts:
    writeThis = str(item) + ': ' + str(counts.get(item)) + '\n'
    wordCounts.write(writeThis)

milton.close()
wordCounts.close()
