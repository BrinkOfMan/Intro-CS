#Day 27

#===============More classes===============

#Fraction class
class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def simplify(self):
        common = gcd(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common

    def add(self,otherfraction):

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den

        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __eq__ (self, f2):
        #Overrides the == operator
        if (self.num * f2.den == f2.num * f1.den):
            return True
        return False
    
    def __add__ (self, f2):
        #Overrides the + operator
        newden = self.den * f2.den
        newnum = self.num * f2.den + f2.num * self.den
        f3 = Fraction(newnum, newdem)
        f3.simplify()
        return f3

    def __lt__ (self, f2):
        #Overrides the < operator
        if sameRational(self, f2):
            return False
        elif (self.num / self.den) < (f2.num / f2.den):
            return True
        return False


#==========End of example fraction==========

#The __len__(self) will override the len() operator

        
def sameRational(f1, f2):
    return f1.getNum()*f2.getDen() == f2.getNum() * f1.getDen()
    
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

f1 = Fraction(3,4)
f2 = Fraction(6,8)
print(f1 == f2)
