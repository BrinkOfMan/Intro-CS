#Ethan Brinkman
#Homework 15: Pirate and Merge
#Due 4/10/2019


#==================Functions needed for the program==================

def removeNonAlpha(astring):
    alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    newstring = ''
    for char in astring:
        if char not in alphabet:
            pass
        else:
            newstring += char
    return newstring


def pirateTranslator(pirateDictionary, inputString):
    newString = ""
    splitString = inputString.split()
    for word in splitString:
        word = removeNonAlpha(word)
        newString += str(pirateDictionary.get(word,word)) + ' '
            
    
    return newString

def merge(d1, d2):
    merged = d1.copy()
    for key in d2.keys():
        if key in merged:
            merged[key] += d2.get(key)
        else:
            merged[key] = d2.get(key)

    return merged

#====================================================================


#Pirate problem:

print('"Hello, how are you?" in pirate speak is:')
pirateWords = {"Hello":"Ahoy", "friend":"matey", "friends":"mateys", \
               "hello":"ahoy", "are":"be", "you":"ye", "my":"me"}
print(pirateTranslator(pirateWords, "Hello, how are you?")) #Ahoy how be ye

#Merger problem:
storage1 = {'oranges': 22, 'bananas': 24, 'apples': 18, 'kiwi': 40}
storage2 = {'oranges': 18, 'bananas': 16, 'apples': 22, 'strawberry': 40}

print('\nCombining the two fruit storages should yield 40 of each fruit.')
print("Let's try:")
print(merge(storage1,storage2))
