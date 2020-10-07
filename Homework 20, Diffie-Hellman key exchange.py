#Ethan Brinkman
#Homework 20: 1 and 2
#Due 4/22/2019


def Diffie(g, p, x):
    secret = g^x % p
    return secret


#=====Number 1=====
print('Number 1:\n')

prime = 67
generator = 2
a = 5
b = 52

AliceToBob = Diffie(generator,prime,a)
BobToAlice = Diffie(generator,prime,b)

print('Alice sends',AliceToBob,'to Bob.')
print('Alice sends',BobToAlice,'to Bob.')
print("Using Bob's secret number, their shared secret number is",Diffie(AliceToBob,prime,b))
print("Using Alice's secret number, their shared secret number is",Diffie(BobToAlice,prime,a))

#=====Number 2=====
print('\nNumber 2:\n')

def isPrime(n):
    import math
    for num in range(2,int(math.sqrt(n)+1)): #Include the square root of the number
        result = n % num
        if (result == 0):
            return False
    return True

print('Is 7 a prime number?: '+str(isPrime(7)))
print('Is 9 a prime number?: '+str(isPrime(9)))
bigNum = 123456
print('Those are easy, what about '+str(bigNum)+'?: '+str(isPrime(bigNum)))
print('Hmm, what if we make that number one higher?')
otherbigNum = 123457
print('TESTING NUMBER '+str(otherbigNum)+': '+str(isPrime(otherbigNum)))

