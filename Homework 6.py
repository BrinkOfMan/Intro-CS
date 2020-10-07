#Ethan Brinkman
#Homework 6: 1, 2, 6, 8
#Due 2/27/2019

#Number 1
print("Number 1\n")

print("3 == 3 evaluates to", 3 == 3)
print("3 != 3 evaluates to", 3 != 3)
print("3 >= 4 evaluates to", 3 >= 4)
print("not (3 < 4) evaluates to", not (3 < 4))

#Number 2
print("\nNumber 2\n")

print("The logical opposite of a > b is a <= b")
print("The logical opposite of a >= b is a , b")
print("The logical opposite of a >= 18  and  day == 3 is a < 18 or day != 3")
print("The logical opposite of a >= 18  or  day != 3 is a < 18 and day == 3")

#Number 6
print("\nNumber 6\n")

def findHypot(a,b):
    c = (a**2 + b**2) ** 0.5
    return c

side1 = float(input("Please input side a and b of a right triangle\nside a: "))
side2 = float(input("side b: "))

print(findHypot(side1,side2), "is the length of the hypotenuse.")

#Number 8
print("\nNumber 8\n")

def is_odd(n):
    if (n % 2 == 0):
        return False
    else:
        return True

testNum = int(input("Please input an integer.\nThe computer will return True if it is odd, and it will return False if it is even.\n"))
print(is_odd(testNum))

input()             #This is to prevent a cmd window from closing immediately

    
