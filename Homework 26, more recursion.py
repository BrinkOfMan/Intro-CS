#Ethan Brinkman
#Homework 26: Tower of Hanoi, Binary Search, and Comment questions



#==========Number 1:==========
print('Number 1:\n')

"""NOTE: I know in class we were only allowed to use start and end
I'm sure there's a way to do it with just start and end, I just
Couldn't figure it out. Using the third variable 'temporary' does work"""

moves = 0
def towerOfHanoi(n, start, end, temp):
    
    global moves
    #I'm using moves just to see if it's correct
    #If it is correct, this should end up being minimum number of moves for each amount of disks

    if n == 1: 
        print ("Move disk",n,"from post",start,"to post",end)
        moves += 1
        
    else:
        towerOfHanoi(n-1, start, temp, end)
        print ("Move disk",n,"from post",start,"to post",end)
        moves += 1
        towerOfHanoi(n-1, temp, end, start)

#now start the program
num = int(input("How many disks will you put on your tower of Hanoi? "))
print('The minimum number of moves for',num,'disks is',(2**num)-1)
towerOfHanoi(num, 1, 3, 2)
print("Finished!", "Number of moves:", moves)

#==========Number 2:==========
print('\nNumber 2:\n')

def binarySearch(alist, item):

    if len(alist)==0:
        return False

    elif alist[len(alist)//2] == item:
        return True

    elif alist[len(alist)//2] < item:
        leftList = alist[len(alist)//2 + 1: ]
        print(item, 'is greater than the middle this list! Seearching within',leftList)
        return binarySearch(leftList,item)

    else:
        rightList = alist[0: len(alist)//2]
        print(item, 'is lesser than the middle of this list! Seearching within',rightList)
        return binarySearch(rightList,item)

aL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
aL = [1,2,3,4,5,6,7]
i = int(input('Please enter a number, and I will see if it is in a secret list I have stored: '))

print('The secret list is', aL)
print('Is',i,'in this list?',binarySearch(aL, i))

#==========Comment questions==========

#The smallest number of moves to solve the tower of hanoi with 4 disks is 15
#The equation for the minimum number of moves is: (2^numDisks - 1)

#With a list of 7 items, my binary search needs to happen at most 3 times for a True, 4 times for a False
##it will not find the item the first 2 times, and either find the item the third time (True) or will not find it two more times (False)
#Using the equation from the book (len(list)/(2^(steps)) = 1, we can calculate
##(len(list) / 2^5 steps) = 1
##(len(list) / 32 steps) = 1
##(len(list)*32)/32 = 32
##len(list) = 32
#Therefore, the maximum list length to get 5 steps should be 32
