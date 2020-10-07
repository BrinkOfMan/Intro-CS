#Ethan Brinkman
#Homework 9: 7, 8, 10, 11, 12
#Due 3/6/2019

import cImage as image

#===================Functions needed to complete homework; later executed in main()===================

#Number 7 function

def noRed(pic, wn):
    newimg = pic
    for col in range(pic.getWidth()):
        for row in range(pic.getHeight()):
            pix = pic.getPixel(col, row)    #get the pix(el) for this specific row and column

            newRed = 0                      #goodbye, red
            newGreen = pix.getGreen()       #green stays normal
            newBlue = pix.getBlue()         #blue stays normal

            newPix = image.Pixel(newRed, newGreen, newBlue)

            newimg.setPixel(col, row, newPix)

    return newimg

#Number 8 function

def grayscale(pic, wn):
    newimg = pic
    for col in range(pic.getWidth()):
        for row in range(pic.getHeight()):
            pix = pic.getPixel(col, row)    #get the pixel for this specific row and column

            grayRed = pix.getRed()          #add the three RGB values up
            grayGreen = pix.getGreen()      #and divide them to get
            grayBlue = pix.getBlue()        #a grayscale effect

            avg = ((grayRed + grayGreen + grayBlue) // 3)    #like this
            newPix = image.Pixel(avg, avg, avg)

            newimg.setPixel(col, row, newPix)

    return newimg
    
#Number 10 function

def sepia(pic, wn):
    newimg = pic
    for col in range(pic.getWidth()):
        for row in range(pic.getHeight()):
            pix = pic.getPixel(col, row)      #get the pixel for this specific row and column

            #Conversions for the sepia effect
            newRed = int(min(255, ((pix.getRed() * 0.393) + (pix.getGreen() * 0.769) + (pix.getBlue() * 0.189))))
            newGreen = int(min(255, ((pix.getRed() * 0.349) + (pix.getGreen() * 0.686) + (pix.getBlue() * 0.168))))       
            newBlue = int(min(255, ((pix.getRed() * 0.272) + (pix.getGreen() * 0.534) + (pix.getBlue() * 0.131))))

            newPix = image.Pixel(newRed, newGreen, newBlue)

            newimg.setPixel(col, row, newPix)

    return newimg

#Number 11 function

def doubleSize(pic, wn):
    
    newimg = image.EmptyImage(pic.getWidth()*2, pic.getHeight()*2)  #Double the size of the new image
    for col in range(pic.getWidth()):                               #Using copy3 size since that's the original image
        for row in range(pic.getHeight()):
            oldPix = pic.getPixel(col, row)                         #the place/RGB of the pixel will be placed 4 times

            newimg.setPixel(2*col, 2*row, oldPix)                   #"original" pixel
            newimg.setPixel(2*col+1, 2*row, oldPix)                 #pixel next to "original"
            newimg.setPixel(2*col, 2*row+1, oldPix)                 #pixel below the "original"
            newimg.setPixel(2*col+1, 2*row+1, oldPix)               #pixel next to the previous

    return newimg

#Number 12 function

def smooth(pic, wn):
    newimg = pic 
    w = pic.getWidth()-1                                            #Using this for the future min function for width
    h = pic.getHeight()-1                                           #Using this for the future min function for height
    for col in range(pic.getWidth()):
        for row in range(pic.getHeight()):
            pix0 = pic.getPixel(col, row)                           #Get the pixel for for this specific row and column
            pix1 = pic.getPixel(min(col+1,w), row)                  #Get the pixel right of the original
            pix2 = pic.getPixel(col, min(row+1,h))                  #Get the pixel below the original
            pix3 = pic.getPixel(min(col+1,w), min(row+1,h))         #Get the pixel at the bottom-right corner
            pix4 = pic.getPixel(max(col-1,0),row)                   #Get the pixel left of the original
            pix5 = pic.getPixel(col,max(row-1,0))                   #Get the pixel above the original
            pix6 = pic.getPixel(max(col-1,0),max(row-1,0))          #Get the pixel at the top-left corner
            pix7 = pic.getPixel(max(col-1,0),min(row+1,h))          #Get the pixel at the bottom-left corner
            pix8 = pic.getPixel(min(col+1,w),max(row-1,0))          #Get the pixel at the top-right corner


            #Averaging the colors out for all 9 pixels (I'm sure there is an easier way to do this, but this is what I got)
            avgR = int((pix0.getRed() + pix1.getRed() + pix2.getRed() + pix3.getRed() + pix4.getRed() + pix5.getRed() + pix6.getRed() + pix7.getRed() + pix8.getRed()) / 9)
            avgG = int((pix0.getGreen() + pix1.getGreen() + pix2.getGreen() + pix3.getGreen() + pix4.getGreen() + pix5.getGreen() + pix6.getGreen() + pix7.getGreen() + pix8.getGreen()) / 9)
            avgB = int((pix0.getBlue() + pix1.getBlue() + pix2.getBlue() + pix3.getBlue() + pix4.getBlue() + pix5.getBlue() + pix6.getBlue() + pix7.getBlue() + pix8.getBlue()) / 9)
            
            avgPix = image.Pixel(avgR, avgG, avgB)
            newimg.setPixel(col, row, avgPix)

    return newimg

#================================end of functions, beginning of main()================================

def main():
    
    img = image.Image("luther.gif")
    copy0 = img.copy()
    copy1 = img.copy()
    copy2 = img.copy()
    copy3 = img.copy()
    win = image.ImageWin('frame', img.getWidth()*2 + 10, img.getHeight()*2 + 10)    #This is so I can fit four images into 1 frame
    img.draw(win)

    print('Number 7\nRed filter')
    copy0 = noRed(copy0, win)                                   #Calls to the function needed for Number 7
    copy0.setPosition(img.getWidth()+10, 0)                     #Places this new image next to the original one
    copy0.draw(win)

    print('\nNumber 8\nGrayscale filter')
    copy1 = grayscale(copy1, win)                               #Calls to the function needed for Number 8
    copy1.setPosition(0, img.getHeight()+10)                    #Places this new image below the original one
    copy1.draw(win)

    print('\nNumber 10:\nSepia filter')
    copy2 = sepia(copy2, win)                                   #Calls to the function needed for Number 10
    copy2.setPosition(img.getWidth()+10, img.getHeight()+10)    #Places this new image next to the grayscale one
    copy2.draw(win)

    print('\nClick on the frame to start the new sequence of image processing.')
    win.exitOnClick()

    win = image.ImageWin('frame', img.getWidth()*2, img.getHeight()*2)
    img.draw(win)
    print('\nNumber 11:\nDoubling the size of the image.')
    copy3 = doubleSize(copy3, win)                              #Calls to the function needed for Number 11
    copy3.draw(win)

    print('\nNumber 12:\nSmoothing the image out.\nThis will take about 60 seconds.')
    copy4 = smooth(copy3, win)                                  #Calls to the function needed for Number 12
    copy4.draw(win)

    print('\nClick on the frame when you are finished with looking at the image.')
    win.exitOnClick()

main()
