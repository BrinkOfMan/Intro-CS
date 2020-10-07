#Day 10 stuff

#Use ipconfig to see a whole buncha stuff
#The IPv6 8 by 4 hexadecimal format doesn't necessarily need to fill all number slots
##IPv6: 0 -> FFFF
##IPv4: 0 -> 255

#use getmac to see mac addresses
##MAC: 00 -> FF

#Use this format
#tracert <destination webstie>
#To find the routers needed to form the connection
#Note: bigger websites will require bigger servers.
##Beause of this, big boi servers may end with the same URL, but different IP addresses

#Important note for infinite loops: hit control+c

#============================================================
import random

def forCoin():
    HeadsCount = 0
    TailsCount = 0
    for i in range(500):
        r = random.randrange(0,2)
        if r == 0:
            HeadsCount += 1
        else:
            TailsCount += 1
            
    print('Total number of "For Heads" flipped:',HeadsCount)
    print('Total number of "For Tails" flipped:',TailsCount)


forCoin()


def whileCoin():
    FlipAgain = 1
    HeadsCount = 0
    TailsCount = 0
    while FlipAgain != 0:
        r = random.randrange(0,2)
        if r == 0:
            HeadsCount += 1
        else:
            TailsCount += 1
        FlipAgain = random.randrange(0, 500)
            
    print('Total number of "While Heads" flipped:',HeadsCount)
    print('Total number of "While Tails" flipped:',TailsCount)


whileCoin()

""" Class demonstration of changing a for i in range(10) into a while loop
i = 0
while i < 10:
    print (i * i)
    i += 1
"""

Sum = 0
i = 0
ctr = 0
while Sum < 1000000:
    Sum += i
    i += 1
    ctr += 1
    
print("It requires",ctr,"summation iterations to reach a million.")

response = int(input("Enter a number, 1-10, please.\n"))
while (response < 0 or response > 10):
    response = int(input("No, a number from a range that includes 1 and 10.\n"))
print("Thanks for entering",response)

#============================================================
