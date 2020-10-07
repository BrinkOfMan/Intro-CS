#Day 9 in-class practice

print("Number 1\n")

def is_vowel(c):
    if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
        return True
    return False
    


def all_vowels(c):

    for i in (c):
        if not(is_vowel(i)):
            return False
    return True

mystring = input("Please enter a string of lowercase letters\n")
print(all_vowels(mystring))
            

