#save this file as request_test.py

import urllib.request

f = urllib.request.urlopen("http://www.mlwright.org/teaching/cs121s17/milton.txt")

print(type(f))

print("URL:", f.geturl())
print("INFO:", f.info())
print("CODE:", f.getcode())

## Keep uncommented to print to the shell
#print(f.read().decode())

## if you instead want to save this file,
## comment out the above print statement, and
## uncomment the following lines
outfile = open("milton.txt", "w")
outfile.write(f.read().decode())
outfile.close()
