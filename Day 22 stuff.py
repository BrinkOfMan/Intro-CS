#Day 22

#Dictionairies = {key1:var1, 'key2':var2, key3:'var3'}

#Assigning a variable to a dictVar will make python reference the same object
##copyVar is dictVar would return True
##Instead, use copyVar = dictVar.copy()

#Since you can't change a key-value pair, you must delete the pair and re-add a different one
##See the first operation

#Operations for dictionairies:

##dictVar[newkey] = newVal will add a key-value pair in the dictVar
##del dictVar[key] will delete the key-value pair in the dictVar
##dictVar.keys() will return a view of the keys in the dictionary
##dictVar.values() will return a view of the values in the dictionary
##dictVar.items() will return a view of the key-value pairs in the dictionary
##dictVar.get(key,alt) will return the value for a key, or alt if no key in the dictionary
###If no alt specified, alt will default to None

def countAlpha(astr):
    counts = {}
    for char in astr:
        if char.isalpha():
            if char.lower() in counts:
                counts[char.lower()] += 1
            else:
                counts[char.lower()] = 1
            
    return counts

thing = 'She sells 20 seashells. She sells them by the seashore!'
print('Here are the total count for all the letters in this string:')
print(thing ,countAlpha(thing))

"""
def merge(d1, d2):
    d3 = {}
    for akey in d1.keys():
        if akey in d2:
            d3[akey] = d1[akey] + d2[akey]
        else:
            d3[akey] = d1[akey]
    for akey in d2.keys():
        if akey in d1:
            pass
        else:
            d3[akey] = d2[akey]

    return d3
"""

def merge(d1, d2):
    d3 = d1.copy()

    for akey in d2.keys():
        if akey in d1:
            d3[akey] += d2[akey]
        else:
            d3[akey] = d2[akey]

    return d3

dict1 = {'apple':1, 'banana':12, 'orange':3, 'starfruit':2}
dict2 = {'apple':4, 'banana':3, 'orange':7, 'durian':5}
print(merge(dict1, dict2))
