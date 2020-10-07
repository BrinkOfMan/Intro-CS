#Ethan Brinkman
#Homework 11: Problems 1, 2, 3, 4


#Number 1
print('Number 1\n')

def countOccurrences(bigstr, substr):
    amount = bigstr.count(substr)
    return amount

print('The number of times','"ss" appears in','"Miss, this is Mississippi" is',countOccurrences('Miss, this is Mississippi','ss'))


#Number 2
print('\nNumber 2\n')

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

print('Removing "cat" from the string "A bobcat is a big cat." gives us the new string:')
print(removeAll('A bobcat is a big cat.','cat'))


#Number 3
print('\nNumber 3\n')

def toPigLatin(s):                      #Only works with a single word
    newstring = ''
    Vowels = 'aeiouAEIOU'
    isVowel = False
    char = 0                            #Setting up the preconditions for the while loop

    if s[0] in Vowels:
            newstring = s+'yay'
            return newstring
            
    while isVowel != True:
        if s[char] in Vowels:
            isVowel = True              #Ends the loop
        else:
            char += 1
        
    newstring = s[char:]+s[0:char]+'ay' #Adding the pieces together
    return newstring

string = input('Insert your favorite word and I will turn it into pig Latin:\n')
print(toPigLatin(string))


#Number 4
print('\nNumber 4\n')

def isEmailAddress(s):
    localPart = 'abcdefghijklmnopqrstuvwxysABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-!+'
    domain = 'abcdefghijklmnopqrstuvwxysABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'

    if '@' in s:
        posAt = s.find('@')              #Skip over if no '@'
        for i in range(posAt):           #Will go until the index '@'
            if s[i] in localPart:
                pass                    #Legal character? Keep going, then.
            else:
                print('An illegal character was found in local art. It was',s[i],'at index',i)
                return False

        for i in range(posAt+1,len(s)):
            if s[i] in domain:
                pass
            else:
                print('An illegal character was found in the domain. It was',s[i],'at index',i)
                return False
        
        return True
    return False
    

email = input('Type a string, and I will see if it is an email address\n')
print(isEmailAddress(email))

input('Hit the enter key to close the program.\n(If you are running in a cmd window)')

