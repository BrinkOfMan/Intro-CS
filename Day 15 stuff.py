#Day 15

#HTTP typically uses port 80
#IMAP (for most emails) uses port 143
#SMTP (another one for emails) uses port 25
#POP3 (barely any emails) uses port
##Grabs emails that are stored on a separate server
#FTP (File transfer protocol) uses ports 20 / 21
##SSH (Secure socket handling) uses port 22

#Some wack shit to make the removeNonAlpha easier
##string.isalpha() returns True is it is a string of alphabetical characters

#Random HTML tidbits that I've forgotten / learned
##Empty elements are sometimes called void elements
##Element, Content, Attributes (go into elements)
##Blocks form a new block of stuff, in-line will follow the same line, and can modify a block


#Practice problem 3 for Monday's stuff:

def makeTag(tag,text):
    Open = '<'+tag+'>'
    close = '</'+tag+'>'
    newstr = Open+text+close
    return newstr

print(makeTag('b','Bold text'))

#And 4:

def extractText(s):
    
    pos0 = s.find('>')
    pos1 = s.find('</')

    newstr = s[pos0 + 1 : pos1]
    return newstr

print (extractText('<b>Hello world</b>'))
