#Day 21

#Methods and stuff for data files

#ALWAYS CLOSE YOUR FILES

#filevar.write(astring)
##will add astring to the end of the file

#filevar.read(n)
##reads and returns a string of n characters, or the entire file as a single string if n is nor provided

#filevar.readline(n)
##returns the next line of the file with all text up to and including the newline character.
##If n is provided as a parameter than only n characters will be returned if the line is longer than n.

#filevar.readlines(n)
##Returns a list of strings, each representing a single line of the file.
##If n is not provided then all lines of he file are returned.
##If n is provided, then n characters are read but n is rounded up so that an entire line is returned.


#filevar.seek(n)
##will go to whatever character at the file

#filevar.tell()
##tells the current position of the marker in the file

myfile = open('numbers.txt', 'r')
file_lines = []
for aline in myfile:
    file_lines.append(aline)
myfile.close()

outfile = open('numbers_sum.txt','w')
for aline in file_lines:
    sum_line = 0
    ints = [int(item) for item in aline.split()]
    for x in ints:
        sum_line += x
    outfile.write(str(sum_line)+'\n')

outfile.close()

myfile = open('milton.txt','r')
text_lines = [myfile.readline() for aline in myfile]
myfile.close()

outfile = open('screaming_milton.txt','w')
for item in text_lines:
    outfile.write(item.upper())
outfile.close()
