#program to encrypt/decrypt using the Caesar cipher

#function to encrypt/decrypt one character
#assume char is alphabetic
def caesarShift(char, num):
    if char.islower():  #lowercase letters have ASCII values 97 to 122
        val = ord(char) - 97 + num
        return chr((val % 26) + 97)
    else:               #uppercase letters have ASCII values 65 to 90
        val = ord(char) - 65 + num
        return chr((val % 26) + 65)


#do some encryption/decryption
original = input("Enter some text: ")
goodShift = False
while goodShift == False:
    try:
        shift = int(input("Enter the shift amount: "))
    except ValueError:
        print("Invalid input, please try again and enter a number.")
    else:
        goodShift = True

transformed = ""

for char in original:
    if char.isalpha():
        transformed = transformed + caesarShift(char, shift)
    else:
        transformed = transformed + char

print(transformed)
