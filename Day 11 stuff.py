#Day 12
#image processing goes by column, row → ↓

#the cImage module has some useful stuff:

#for image processing:
##ImageWin(name, #cols, #rows) will create a window with the name, #cols, #rows
##getWitdh() wil return the width of the image in pixels
##getHeight() will return the height of the image in pixels
##setPosition(col#, row#) will se the start of a draw at col#, row#
##getPixel(col#,row#) will return the pixel at col#, row#
##setPixel(col#,row#,p) will set the pixel at col# row# to have a value of p
##copy() will copy the image to another variable
##draw(windowname) will draw the image in the windowname

#for pixel processing:
##pixel(r#,g#,b#) will create a new pixel with r g b values 0-255
##getRed()/getGreen()/getBlue() will return the r/g/b component intensity
##setRed()/setGreen()/setBlue() will se the r/g/b component intensity

from cImage import *

def invertImage(myImage):
    for row in range(myImage.getHeight()):
        for col in range(myImage.getWidth()):
             v = myImage.getPixel(col,row)
             v.red = 255 - v.red
             v.green = 255 - v.green
             v.blue = 255 - v.blue
             myImage.setPixel(col,row,v)

def removeBlue(myImage):
    for row in range(myImage.getHeight()):
        for col in range(myImage.getWidth()):
            v = myImage.getPixel(col, row)
            v.setBlue(0)
            myImage.setPixel(col,row,v)
            pass

def makeRed(myImage):
    for row in range(myImage.getHeight()):
        for col in range(myImage.getWidth()):
            v = myImage.getPixel(col,row)
            v.blue = 0
            v.green = 0
            myImage.setPixel(col,row,v)
            pass

def main():
    win = ImageWin("My Window",1200,800)
    oImage = FileImage('kitten.gif')
    print(oImage.getWidth(), oImage.getHeight())
    oImage.draw(win)
    myImage1 = oImage.copy()
    myImage2 = oImage.copy()
    myImage3 = oImage.copy()

    invertImage(myImage1)        
    myImage1.setPosition(myImage1.getWidth()+10,0)  #Sets the image 10 pixels away
    myImage1.draw(win)

    removeBlue(myImage2)
    myImage2.setPosition(0, myImage2.getHeight()+10)
    myImage2.draw(win)
    

    makeRed(myImage3)
    myImage3.setPosition(myImage3.getWidth()+10, myImage3.getHeight()+10)
    myImage3.draw(win)

    #print(win.getMouse())
    #myImage1.save('lcastle-inverted.gif')
    #print(myImage1.toList())

    win.exitOnClick()
main()


