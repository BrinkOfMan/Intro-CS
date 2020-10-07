#Ethan Brinkman
#Homework 16: 1 and 2
#Due 4/12/2019

#==============================Number 1:==============================
print('Number 1\n')

try:
    fileName = input('Please type in the name of a file you want to open: ')
    fileData = open(fileName, 'r')
    print("\nThe file was opened successfully. Let's see what's in it.\n")
    for aline in fileData:
        print(aline)
        
except FileNotFoundError:
    print("Looks like we weren't able to open that file because it wasn't found.")
    print('Did you type it in correctly? Restart and try again.')
    

#==============================Number 2:==============================
print('\nNumber 2\n')

def A(a_list):
    try:
        return B(a_list)
    except TypeError:
        return('Looks like we have a type error. Make sure all integers you send to A are integers, not written out numbers.')
    except:
        return("Something went wrong and I don't know what.")

def B(b_list):
    s = 0
    for i in b_list:
        s += i
    return s
        

print(A([1,2,3]))
print(A([1,'two',3]))
