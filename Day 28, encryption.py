#Day 28

#Assymetric
#Key encryption
#algorithm
#Shared public key
#Private key
#Encrypt -> Decrypt, Sign -> Verify

#Diffie-Hellman
##Works over unsecured networks at sending secured messages
##g = generator, p = prime, n = positive integer, x = personal secret number

##(g^x) mod p = n

#Diffie-Hellman example:
##Alice and Bob
##p = 31, g = 11

##Round 1
##Alice: a (secret number) = 16, Alice to Bob = g^a mod p = 20
##Bob: b (secret number) = 4, Bob to Alice = g^b mod p = 9

##Round 2
##SecretAlice = (g^b mod p)^a = 9^16 mod 31 = 9
##SecretBob = (g^a mod p)^b = 20^4 mod 31 = 9


prime = 47
generator = 5
ethan = 37
def Diffie(g, p, x):
    secret = g^x % p
    return secret

print(Diffie(generator, prime, ethan))

NtoE = 42

secret = 42^37 % 47

print(secret)

def isPrime(n):
    for num in range(2,n//2):
        result = n % num
        if (result == 0):
            return True
    return False

print(isPrime(10))

