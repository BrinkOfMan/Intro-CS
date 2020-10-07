#Ethan Brinkman
#Homework 19: problems 7, 8, 10, 12 from the book, robot
#Due 4/19/2019

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


#==========Rectangle class (from book problems)==========

class Rectangle:
    def __init__(self, posLLC, width, height):
        self.loc = posLLC
        self.w = width
        self.h = height
        
    def __str__(self):
        return ('Position of lower-left corner: '+str(self.loc)+'\nWidth: '+str(self.w)+'\nHeight: '+str(self.h))

    def getWidth(self):
        return self.w

    def getHeight(self):
        return self.h

    def perimeter(self):
        return 2*self.w + 2*self.h
    
    def contains(self,point):
        xrange = (self.loc.getX(), self.loc.getX() + self.w)
        yrange = (self.loc.getY(), self.loc.getY() + self.h)
        if (point.getX() >= xrange[0] and point.getX() <= xrange[1]) and (point.getY() >= yrange[0] and point.getY() <= yrange[1]):
            return True
        return False
    
#=====================================


#Number 7:
r = Rectangle(Point(4, 5), 6, 5)

#Number 8:
print(r)
print('\nThe weidth of your rectangle is:',r.getWidth())
print('\nThe height of your rectangle is:',r.getHeight())

#Number 10:
print('\nThe perimeter of your rectangle is:',r.perimeter())

#Number 12:
print('\nIs the point (5,6) in your rectangle?:',r.contains(Point(5,6)))
print('Is the point (9,10) in your rectangle?:',r.contains(Point(9,10)))
print('Is the point (0,0) in your rectangle?:',r.contains(Point(0,0)))
print('Is the point (-5,-5) in your rectangle?:',r.contains(Point(-5,-5)))
print('Is the point (4,5) in your rectangle?:',r.contains(Point(5,6)))
print('Is the point (12,6) in your rectangle?:',r.contains(Point(12,6)))
print('Is the point (7,3) in your rectangle?:',r.contains(Point(7,3)),'\n')

#==============Robot class==============

class Robot:
    def __init__(self,Name,build_year):
        self.name = Name
        self.buildYr = build_year
        self.battery = 0

    def introduce(self):
        return('Hello, I am '+self.name+'.')

    def charge(self):
        print('The battery is charging.')
        self.battery = 100
        
    def __str__(self):
        return(self.name+' was built in '+str(self.buildYr)+' and has '+str(self.battery)+'% battery left.')
    

rob = Robot('Rob',2019)
print(rob.introduce())
print('The battery is currently at '+str(rob.battery)+'%.')
rob.charge()
print('The battery is currenetly at '+str(rob.battery)+'%.')
print(rob)
