#Day 23

#An exception is a message to any function currently on the executing program's "run-time-stack"
##Any message that something "out-of-the-ordinary" has happened and the flow-of-control needs to be abandoned
##Can be used to communicate directly with other functions, instead of having to go through multiple functions
##The "run-stime-stack" is what keeps track of the active function calls while a program is executing.

#Use the raise ExceptionName command to create an exception
##This will interrup the normal flow-of-control, and Python will look for any code in its run-time-stack that is
##interested in dealing with the message
###It will start searching from the bottom towards the top of the run-time-stack (opposite of the order which functions were called)
###The first try: except: block that python finds on its search will be executed.
###If there is no try: except: block found, the program "crashes" and prints its run-time-stack to the console

#Example stuff
#try:
#   funcA()
#except anException:        #Will execute if the MyException message happened

#def A():
#   Stuff()
#   B()

#def B():
#   Stuff()
#   if something_special_happened:
#       raise anException

#Here is the link that lists all of the exceptions, and the hierarchy they appear in:
#https://runestone.academy/runestone/static/CS121/Exceptions/02_standard_exceptions.html
##The most generic one to use is 'Exception', as it holds practically every other exception type there is
##You can also just have the command except:

#If your try: except: block is in the same function that raises the exception, you are probably mis-using exceptions.

#Some principles to using exceptions:

##If a condition can be handled using the normal flow-of-control, don’t use an exception!

##If you call a function that potentially raises exceptions, and you can do something appropriate to deal with the exception,
##then surround the code that contains the function call with a try: except: block.

##If you call a function that potentially raises exceptions, and you can’t do anything meaningful about the conditions
##that are raised, then don’t catch the exception message(s).

#Here's a link for syntax, since I'm too lazy to write them all down:
#https://runestone.academy/runestone/static/CS121/Exceptions/04_exceptions_syntax.html


#===================================Class time===================================
try:
    F = open('C:/Users/Ethan/Desktop/nativelog.txt', 'r')
except FileNotFoundError:
    print('File not found')
else:
    Flines = F.readlines()
    print(Flines)





