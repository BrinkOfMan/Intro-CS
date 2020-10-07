#Day 13

#Strings and stuff
##You can't change a string, you can only return new strings and set a string to the new one
###(Immutable)
##Indexing strings goes (from L -> R) 0 - end, (from L <- R) -end - -1
##Using the [] will find the character at an index
###you an also do stuff like:
#h= "hello"
#print(h[1:4]) and it will print "ell" (indexes 1, 2, 3)

#Some commands using strings
##upper(none) returns a string in all uppercase
##lower(none) returns a string in all lowercase
##capitalize(none) returns a string with the first character capitalized, the rest lower
##strip(none) returns a string with the leading and trailing whitespace removed
##lstrip(none) returns a string with the leading whitespace removed
##rstrip(none) returns a string with the trailing whitespace removed
##count(item) returns the number of occurences of item
##replace(old,new) replaces all occurences of old substring with new
##center(width) returns a string centered in a field of width spaces
##ljust(width) returns a string left justified in a field of width spaces
##rjust(width) returns a string right justified in a field of width spaces
##find(item) returns the leftmost index where the substring item is found, or -1 if not found
##rfind(item) returns the rightmost index where the substring item is found, or -1 if not found
##index(item) same as find() except it causes a runtime error if item is not found
##rindex(item) same a rfind() except it causes a runtime error if item is not found
##format(substitutions) is special, ex:
#person = input('your name: ')
#print('hello {}!'.format(person))
###use {:.#f} to round to significant figures
###can use format with multiple substitutions

#====================Okay, program time====================

#Write a program that asks the user to type in some text
##then the program reports the number of characters and the number of vowels that the user entered.
vowels = 'aeiouAEIOU'
test = input('input a string of characters, please\n')
testLen = len(test)
ctr = 0
for char in test:
    if char in vowels:
        ctr+=1
    else:
        pass
con = (testLen - ctr)

if ctr == 1:
    if con == 1:
        print('You entered',ctr,'vowel and',con,'consonant.')
    else:
        print('You entered',ctr,'vowel and',con,'consonants.')
elif ctr > 1:
    if con == 1:
        print('You entered',ctr,'vowels and',con,'consonant.')
    else:
        print('You entered',ctr,'vowels and',con,'consonants.')
