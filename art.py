import binascii
import math
import turtle

# globals
FONT_SIZE = 8
FILE_NAME = "LOZ_Secret.wav"
DATA_OFFSET = 44

# basic setup
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
yIncrement = FONT_SIZE + ((charSpaceWidth - charWidth)*2)

# using the charSpaceWidth would make it appear as if text is being normally typed
xIncrement = charSpaceWidth

# starting positions of x and y, (0, 0) would be the ceneter of the screen
startX = (-wn.window_width()/2)
startY = (wn.window_height()/2) - yIncrement

# minus 2 for padding left and right
charactersPerLine = (wn.window_width()/xIncrement) - (2) - 1
numberOfLines = (wn.window_height()/yIncrement) - 1

with open(FILE_NAME,"rb") as f:
    block = f.read()

    # where to start reading the data from
    blockStart = 0 + DATA_OFFSET 

    # how many values to read
    blockIncrement = int(math.floor(charactersPerLine))

    # end of the values to be read
    blockEnd = blockStart + blockIncrement

    # interate from blockStart until the image is filled
    for i in range (blockStart, (int(charactersPerLine) * int(numberOfLines) + blockStart)):

        # when done writing down the line's values, move turtle to the next line
        if (i == blockEnd):
            startX = (-wn.window_width()/2)
            startY -= yIncrement
            blockEnd += blockIncrement

        # write each value
        startX += xIncrement
        tess.penup()
        tess.goto(startX, startY)
        tess.pendown()
        tess.write("0", font=("Courier", FONT_SIZE, "normal"))
        #tess.write(binascii.hexlify(block[i]), font=("Courier", fontSize, "normal"))

# wait for a user click on the canvas
wn.exitonclick()


        