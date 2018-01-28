import binascii
import math
import turtle
from Tkinter import *
from PIL import Image

# globals
FONT_SIZE = 4
FILE_NAME = "input.wav"     # Name of file to get hex values from
IMAGE_NAME = "input.png"    # Name of image file
DATA_OFFSET = 32            # Where to start reading data from (mp3 music data starts at 32 by)

# basic setup
img = Image.open(IMAGE_NAME)
image = img.load()
turtle.setup(img.size[0],img.size[1])
wn = turtle.Screen()
tess = turtle.Turtle()

# determine the width of each character
tess.hideturtle()
tess.goto(0, 0)
tess.write("0", True, font=("Courier", FONT_SIZE, "normal"))
charWidth = tess.xcor()
tess.undo()

# determine the width between each character
tess.goto(0, 0)
tess.write("00", True, font=("Courier", FONT_SIZE, "normal"))
charSpaceWidth = tess.xcor() - charWidth
tess.undo()

# the Y increment per line -- ((charSpaceWidth - charWidth)*2) should add some 
# nice padding but can be changed to whatever to best fit the image 
yIncrement = FONT_SIZE # + ((charSpaceWidth - charWidth)*2)

# using the charSpaceWidth*2 would make it appear as if text is being normally typed
xIncrement = (charSpaceWidth * 2)

# starting positions of x and y, (0, 0) would be the ceneter of the screen
startX = (-wn.window_width()/2)
startY = (wn.window_height()/2) - yIncrement

# minus 2 for padding left and right
charactersPerLine = (wn.window_width()/xIncrement) - 1
numberOfLines = (wn.window_height()/yIncrement) - 1

with open(FILE_NAME,"rb") as f:
    block = f.read()

    # where to start reading the data from
    blockStart = 0 + DATA_OFFSET 

    # how many values to read
    blockIncrement = int(math.floor(charactersPerLine))

    # end of the values to be read
    blockEnd = blockStart + blockIncrement

    # current position of the image 
    imgX = 0
    imgY = 0

    # interate from blockStart until the image is filled
    for i in range (blockStart, (int(charactersPerLine) * int(numberOfLines) + blockStart)):

        # when done writing down the line's values, move turtle to the next line
        if (i == blockEnd):
            startX = (-wn.window_width()/2)
            startY -= yIncrement
            blockEnd += blockIncrement
            imgY += yIncrement
            imgX = 0

        # write each value
        startX += xIncrement
        tess.penup()
        tess.goto(startX, startY)
        tess.pendown()

        img_r = 0
        img_g = 0
        img_b = 0
        img_a = 0

        # get the average color for the segment
        for x in range (imgX, imgX + xIncrement):
            for y in range (imgY, imgY + yIncrement):
                img_r += image[x,y][0] 
                img_g += image[x,y][1] 
                img_b += image[x,y][2] 
                img_a += image[x,y][3] 
        img_r /= (xIncrement * yIncrement)
        img_g /= (xIncrement * yIncrement)
        img_b /= (xIncrement * yIncrement)
        img_a /= (xIncrement * yIncrement)

        imgX += xIncrement

        # if the average color is transparent or white, don't display it
        if (img_a == 0 or (img_r == 255 and img_g == 255 and img_b == 255)):
           continue
        else:
           tess.color(img_r/255.0, img_g/255.0, img_b/255.0)

        # write the next hex value with the corresponding average segment color
        tess.write(binascii.hexlify(block[i]), font=("Courier", FONT_SIZE, "normal"))

cv = tess.getscreen()
cv.getcanvas().postscript(file="output.ps", colormode='color')

# wait for a user click on the canvas
wn.exitonclick()


        