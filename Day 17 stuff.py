#Day 17 (Spring break starts after class let's go)

#Alright, kiddo, it's time for lists:
#Lists, unlike strings, are mutable
##ex: a = [0, 1, 2, 3, 4]
##a[3] = 'chicken'
##a is now [0, 1, 2, 'chicken', 4]
#There is other shit you can do, but I'll get to that later (hopefully)

#Other list commands
##sort()
##append(value)
##del[idx]

#the is operator looks at if something points to the same memory ID as something else


alist = [8, 6, 7, 5, 3, 0 ,9]
def findmin(n):
    placeholder = n[0]
    for i in range(len(n)):
        if n[i] < placeholder:
            placeholder = n[i]
        else:
            pass
    return placeholder

print(findmin(alist))


alist = [8, 6, 7, 5, 3, 0 ,9]
def issorted(n):
    placeholder = n[0]
    for i in range(len(n)):
        if n[i] > placeholder:
            print('Not sorted')
            return False
        else:
            pass
    return True


