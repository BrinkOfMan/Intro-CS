
s = "St. Olaf College"
# slice to get c = "College"
c = s[9:]
print(c)

l = "Luther"
# combine to make l2 = "Luther College"
twelve = l + ' College'
print(twelve)

# combine part of s with l to get l3 = "Luther College"
thirteen = l + ' ' + c
print(thirteen)

x = s[0:9] + " " + c
# what is stored in x?  
print(x)

m11 = ["hello", "ten", [10, 4, 5, 100], [20, 30, 40], "cat"]
# write the list comprehension to create a list containing only strings

m12 = [item for item in m11 if type(item)==str]
print(m12)

# what does ml1[3][1] produce? 
print(m11[3][1])

# what does ml2[1][2] produce? 
print(m12[1][2])

# what does print("cat" in ml2) produce?
print("cat" in m12)



names = ["Anne", "Geoffrey", "Ian", "Koleen", "Henry", "Jennifer"]
ages = [12, 13, 11, 12, 12, 13]

# Function: Merge two lists into a dictionary
# Arguments: lis1, lis2, both lists, of the same length
# Returns: dict1, a dictionary that has keys from lis1, and values from lis2
# Example Output: mergeListsToDict(names, ages) returns the following dictionary:
# {"Anne": 12, "Geoffrey": 13, "Ian": 11, "Koleen": 12, "Henry":12, "Jennifer":13}
def mergeListsToDict(lis1, lis2):
    pass

print(mergeListsToDict(names, ages))








