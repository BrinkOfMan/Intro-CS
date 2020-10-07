#Ethan Brinkman
#Homework 7: Numbers 10 and 12, also the two moodle exercises
#Due 2/29/2019

#Number 10
print("Number 10\n")

def is_rightangled(a,b,c):
    closeEnough = (c**2)-(a**2 + b**2)      #If a^2 + b^2 == c^2, then closeEnough should be about 0
    closeEnough /= c**2                     #Making closeEnough more forgiving when calculating higher numbers. (a=3 b=4 c=5.01 vs. a=300 b=400 c=501)
    if (closeEnough < 0.025 and closeEnough >= -0.025):
        return True
    return False

s1 = float(input("Enter side 1 of your triangle\n"))
s2 = float(input("Enter side 2 of your triangle\n"))
s3 = float(input("Enter side 3 of your triangle\n"))

print("True or False: side lengths", s1, s2, "and", s3, "make up a right triangle.")
print(is_rightangled(s1,s2,s3))


#Number 12
print("\nNumber 12\n")

def is_leap(yr):
    if yr%4==0:
        if yr%100==0:
            if yr%400==0:
                return True         #This year is divisible by 4, 100, and 400.
                                
            return False        #This year is divisible by 4 and 100, but not by 400.
        
        return True         #This year is ivisible by 4, but not by 100.
    
    return False        #This year is not divisible by 4.

year = int(input("Please enter a year.\nThe computer will tell you if it is a leap year (True) or not (False)\n"))
print(is_leap(year))


#Moodle exercise 1
print("\nMoodle exercise 1\n")

def daysInMonth():
    month = int(input("""In "1=(Jan) up to 12=(December)" format, what month is it?\n"""))
    year = int(input("What year is it?\n"))
    
    if month == 2:
        if is_leap(year):
            print("That month will be 29 days long.")
            
        else:
            print("That month will be 28 days long.")
            
    elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        print("That month will be 31 days long.")
    else:
        print("That month will be 30 days long.")
    
daysInMonth()

#Moodle exercise 2
print("\nMoodle exercise 2\n")

def yearAt100():
    birthMonth = int(input("""In "1=(Jan) up to 12=(December)" format, what month is your birthday?\n"""))
    age = int(input("What is your current age?\n"))
    curM = 3                    #Current month
    curYr = 2019                #Current year
    
    if birthMonth <= curM:       #Already had their birthday
        print("You will turn 100 in the year",(100-age)+curYr)

    else:
        print("You will turn 100 in the year",(99-age)+curYr)

yearAt100()
