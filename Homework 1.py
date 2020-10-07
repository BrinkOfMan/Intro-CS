###Ethan Brinkman
###Homework for Wednesday, February 13th
###Numbers 1, 2, 4, 5, 6 from Section 2.13

print("Question 1")#Number 1

print(5 ** 2)   #Agreement between computer and myself (25)
print(9 * 5)    #Agreement between computer and myself (45)
print(15 / 12)  #Agreement between computer and myself (1.25)
print(12 / 15)  #Agreement between computer and myself (0.8)
print(15 // 12) #Agreement between computer and myself (1)
print(12 // 15) #Agreement between computer and myself (0)
print(5 % 2)    #Agreement between computer and myself (1)
print(9 % 5)    #Agreement between computer and myself (4)
print(15 % 12)  #Agreement between computer and myself (3)
print(12 % 15)  #Agreement between computer and myself (12)
print(6 % 6)    #Agreement between computer and myself (0)
print(0 % 7)    #Agreement between computer and myself (0)

print("Question 2")#Number 2

#2 + (3-1) * 10 / 5 * (2 + 3)
#Complete (3-1)=2 and (2+3)=5 first; 2 + (2) * 10 / 5 * (5)
#Then (2)*10=20; 2 + 20 / 5 * (5)
#Then 20/5=4; 2 + 4 * (5)
#Then 4*(5)=20; 2 + 20
#Then 2+20=22; 22 is the final answer.
print(2 + (3 - 1) * 10 / 5 * (2 + 3))

print("Question 4")#Number 4

CurrentDay = int(input("What is the current day (using numbers 0-6, where 0 is Sunday and 6 is Saturday)? ")) 
Holidays = int(input("How many days will you be away for holiday? "))
ReturnDay = (Holidays + CurrentDay) % 7
print("It will be day number",ReturnDay,"when you get back. Enjoy your stay!")

print("Question 5")#Number 5

All = "All "
Work = "work "
And = "and "
No = "no "
Play = "play "
Makes = "makes "
Jack = "Jack "
A = "a "
Dull = "dull "
Boy = "boy."
print("with concactenation of variables:",All+Work+And+No+Play+Makes+Jack+A+Dull+Boy) #This is printed using concactenation of string variables.
All1 = "All"
Work1 = "work"
And1 = "and"
No1 = "no"
Play1 = "play"
Makes1 = "makes"
Jack1 = "Jack"
A1 = "a"
Dull1 = "dull"
Boy1 = "boy."
print("With listing variables:",All1,Work1,And1,No1,Play1,Makes1,Jack1,A1,Dull1,Boy1) #This is printing a list of string variables.

print("Question 6")#Number 6

print(6 * (1 - 2)) #Adding the parenthesis around the expression "1 - 2" gives it priority over the original "6 * 1" expression.
