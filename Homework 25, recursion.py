#Ethan Brinkman
#Homework 25: 1, 2, 3
#Due 5/8/2019

#==========Number 1==========
print('Number 1:\n')

def revList(list1):
    if len(list1) == 0:
        #Checks for when the list is done being reversed
        return list1
    else:
        print('Calling for a recursion with the current list at',list1)
        return [list1[-1]] + revList(list1[:-1])
        #Returns a list starting from position -1 and adds up to that position
    
myList = [1, 2, 3, 'a', 'b', 'c']
print ('The opposite of the list:',myList,'is:',revList(myList))

#==========Number 2==========
print('\nNumber 2:\n')

def isPalindrome(inputString):
    if len(inputString) < 1:
        #A single letter / no letters is considered a palindrome
        return True
    
    elif inputString[0] == inputString[-1]:
        #Second case, the first and last letter should be the same before doing any recursion
        return isPalindrome(inputString[1:-1])
        #If they are, test the next letter
    
    else:
        return False


palindrome = 'racecar'
notAPalindrome = 'apple'
print('Is',palindrome,'a palindrome?',isPalindrome(palindrome))
print('Okay, cool. How about '+notAPalindrome+'? '+str(isPalindrome(notAPalindrome)))

#==========Number 3==========
print('\nNumber 3:\n')

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        #The term in sequence is equal to the sum of the previous two numbers

print('The 4th term of the fibonacci sequence is',fibonacci(4))
print('The 15th term of the fibonacci sequence is',fibonacci(15))
print('The 22nd term of the fibonacci sequence is',fibonacci(22))
