#Day 36

#Tower of Hanoi puzzle:
#  Let disk 1 be the smallest, disk 2 be the second-smallest, etc.
#  Let the posts be labeled 1, 2, 3.
#  Disks start on post 1, and end on post 3.
#  HINT: If called with n, start, and end
#   Base case: if n == 1
#       Move disk n from start post to end post
#   Otherwise:
#       Step 0: calculate which is the temp post
#       Step 1: recursive call to move n-1 disks from start post to temp post
#       Step 2: move disk n from start post to end post
#       Step 3: recursive call to move n-1 disks from temp post to end post

#recursive function to PRINT the steps required to move the n-smallest disks
#  from the "start" post to the "end" post


def towerOfHanoi(n, start, end, temp): 
    if n == 1: 
        print ("Move disk",n,"from rod",start,"to rod",end)
        
    else:
        towerOfHanoi(n-1, start, temp, end) 
        print ("Move disk",n,"from rod",start,"to rod",end)
        towerOfHanoi(n-1, temp, end, start) 

#now start the program
num = int(input("How many disks? "))
towerOfHanoi(num, 1, 3, 2)
print("DONE")

