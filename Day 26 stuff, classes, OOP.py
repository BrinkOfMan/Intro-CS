#Day 26

#==========Classes, OOP==========

#You should, for the sake of mentally keeping track of things, treat classes as proper nouns
##"Point" instead of "point" when naming the class Point

#Classes have states (for turtle, state was position, color, direciton)
##and methods (forward(),right())

#Here's a general syntx of setting up a class:
"""
class Point:
    #Point class for representing and manipulating x,y coordinates.

    def __init__(self, initX, initY):
        #Create a new point at the given coordinates.
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
"""
#Note:Every class should have a method with the special name __init__. This initializer method,
##AKA the constructor, is automatically called whenever a new instance of Point is created.

#Note:The __str__ method is responsible for returning a string representation as defined by
##the class creator.

#We have been using objet-oriented programming (OOP) all along, we just haven't been aware of it
##"hello".upper : "hello" = str object, . = dot, upper() = method

import cImage as image

class Cat:

    def __init__(self, n, a, b):    #Keep these names separate from the assignments
        self.name = n               #Otherwise, this could be confusing
        self.age = a
        self.breed = b
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def breedAge(self):
        return self.breed
        
    def pet(self):
        return str(self.name)+" appreciates your pets and thanks you."

    def __str__(self):
        return "name: "+str(self.name)+", age: "+str(self.age)+", breed: "+str(self.breed)

catVars = input('Please enter a cat name, age, and breed in the format of: "name, age, breed"\n')
splitVars = catVars.split(', ')
catName = splitVars[0]
catAge = splitVars[1]
catBreed = splitVars[2]

myCat = Cat(catName,catAge,catBreed)
print('I have now created a Cat object for you; rest assured knowing it will exist in this program for as long you keep it open.')
print('Here is your cat object:\n'+str(myCat))
if catName == 'garfield' or catName == 'Garfield':
    img = image.Image('garfield_is_fat.gif')
    win = image.ImageWin('Garfield', img.getWidth(), img.getHeight())
    img.draw(win)
    

petResponse = input('\nWould you like to pet '+myCat.getName()+'? y/n\n')
if petResponse == 'y':
    print(myCat.pet())
    img = image.Image('garfield_pet.gif')
    img.draw(win)
elif petResponse =='n':
    print("That's okay, there's always another time to pet your cat.")
else:
    print("I have no idea how to interpret that, but okay.")

    


        
