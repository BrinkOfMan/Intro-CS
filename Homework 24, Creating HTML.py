#Ethan Brinkman
#Homework 24: Colors and Powers
#Due 5/3/2019

import webbrowser, os.path

#===========================Code to write the colors webpage===========================

def strToFile(text, fn):
    """Write a file with the given name and the given text."""
    output = open(fn,"w")
    output.write(text)
    output.close()
    

contents = """<!DOCTYPE html>
<html>
<head>
  <title>Colors</title>
</head>
<body>
"""
#Creating all 8 lines for colors and appending the string to the contents
for i in range(8):
    value = (255//8)*i
    contents = contents[0:]+'<p style="margin: 0px; font-family:impact; font-size:200%; color: white; background-color: rgb(0,'+str(value)+',0)">Red 0, Green '+str(value)+', Blue 0</p>'

contents = contents[0:]+"</body></html>"


#the filename for the HTML file to b5e created
filename = "colors.html"

#write the HTML contents to a file
strToFile(contents, filename)

#open the HTML file in the default browser
webbrowser.open("file:///" + os.path.abspath(filename))

#=================================To the powers webpage================================


def strToFile2(text, fn):
    output2 = open(fn,"w")
    output2.write(text)
    output2.close()

contents2 = """<!DOCTYPE html>
<html>
<head>
  <title>Powers</title>
</head>
<body>
<h1>Powers of 4</h1>
"""
#Creating all 8 lines for powers and appending the string to the contents
for i in range(8):
    contents2 = contents2[0:]+"<p style='font-size:120%'>4<sup>"+str(i)+" = "+str(4**i)+"</p>"
 
contents2 = contents2[0:]+"</body></html>"

#the filename for the HTML file to be created
filename2 = "powers.html"

#write the HTML contents to a file
strToFile2(contents2, filename2)

#open the HTML file in the default browser
webbrowser.open("file:///" + os.path.abspath(filename2))

