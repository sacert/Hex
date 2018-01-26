import binascii
import math
import sys,getopt
import turtle

fontHeightToWidthRatio = 0.645
fontSize = 8
yIncrement = fontSize+2
xPadding = fontSize*fontHeightToWidthRatio
yPadding = yIncrement #2 is buffer

wn = turtle.Screen()

startX = (-wn.window_width()/2)
startY = (wn.window_height()/2) - yPadding

charactersPerLine = ((wn.window_width()/ (xPadding*0.75)) - (xPadding*4.5))/3
numberOfLines = (wn.window_height()/yPadding) - (2)

tess = turtle.Turtle()
tess.hideturtle()

print wn.window_width()


filename = "LOZ_Secret.wav"
blocksize = 1024

opts,args = getopt.getopt(sys.argv[1:],'f:b:')
for o,a in opts:
	if o == '-f':
		filename = a
	if o == '-b':
		blocksize = a

offset = 44
with open(filename,"rb") as f:
    block = f.read()
    str = ""
    start = 0 + offset
    eol = 100000
    endIncrement = int(math.floor(charactersPerLine))
    end = start + endIncrement
    for i in range(start, int(charactersPerLine*numberOfLines)):
        if (i == end):
            yPadding += yIncrement
            startX = (-wn.window_width()/2)
            startY = (wn.window_height()/2) - yPadding
            end += endIncrement
        startX += xPadding*2.5
        tess.penup()
        tess.goto(startX, startY)
        tess.pendown()
        tess.write(binascii.hexlify(block[i]), font=("Courier", fontSize, "normal"))
        #print binascii.hexlify(block[i]) + " "

wn.exitonclick()                # wait for a user click on the canvas

        