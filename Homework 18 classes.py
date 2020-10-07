#Ethan Brinkman
#Homework 18: 1-5
#Due 4/17/2019

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    #Method for problem 1:
    def is_origin(self):
        if self.x == 0 and self.y == 0:
            return True
        else:
            return False

    #Method for problem 2:
    def slope_from_origin(self):
        if self.y == 0:
            return (self.y)
        elif self.x == 0:
            return None
        else:
            return self.y / self.x

    #Method for problem 3:
    def reflect_x(self):
        reflectX = Point(self.x, self.y * -1)
        return reflectX

    #Method for problem 4:
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        return self

    #Method for problem 5:
    def add(self, p2):
        finalP = Point(self.x + p2.x, self.y + p2.y)
        return finalP
        
    
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


resp = input('Enter some coordinates in the format "x, y":\n')
resp = resp.split(', ')
if len(resp) == 2:
    for idx in range(2):
            resp[idx] = int(resp[idx])
                                    
p = Point(resp[0],resp[1])

#Call for problem 1:
print('\nIs your point at the origin (0,0)?:',p.is_origin())

#Call for problem 2:
print('\nThe slope from the origin (0,0) is:',p.slope_from_origin())

#Call for problem 3:
print('\nThe x-reversal of your point is:',p.reflect_x())

#Call for problem 4:
Mresp = input('\nEnter how far you want to move your point in the format "x, y":\n')
Mresp = Mresp.split(', ')
if len(Mresp) == 2:
    for idx in range(2):
            Mresp[idx] = int(Mresp[idx])
print('Your point is now at the coordinates:',p.move(Mresp[0],Mresp[1]))

#Call for problem 5:
resp = input('\nEnter some coordinates for a new point the format "x, y":\n')
resp = resp.split(', ')
if len(resp) == 2:
    for idx in range(2):
            resp[idx] = int(resp[idx])
                                    
p2 = Point(resp[0],resp[1])
print(p2)
p3 = p.add(p2)
print('Combining the first and second points to make a third point, we get:',p3)
