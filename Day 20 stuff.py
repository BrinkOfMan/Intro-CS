#Day 20
#The general expression for a list comprehension is as follows
##[action for item in alist if condition]
#This is useful for increasing the level of conciseness in your code
##Combine the for loop, conditional, and action into one line

alist = [1, 2, 3, 4, 5, 6]
print (alist)
blist = [n**2 for n in alist if n%2 == 0]
#This will fill in blist with the squares for all even numbers in alist
##Shortens to one line of code, instead of having this hunk of code:
### blist = []
### for item in list:
###     if item%2 == 0:
###         blist.append(item**2)
print(blist)

#Tuples are immutable, whereas lits are mutable
##A list called alist[1,2,3,4,5] can be changed with alist[3] = 42
##A tuple alled blist(1,2,3,4,5) can not be changed with alist[3] = 42

a = 1
b = 2

#Tuple assignment can be used to bypass a temporary variable
##temp = a
##a = b
##b = temp

print('Before tuple assignment, a =', a, 'b =', b)
(a,b) = (b,a)
print('After tuple assignment, a =', a, 'b =', b)
