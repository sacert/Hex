# Hex
Reproducing images using hex values found from a desired file 

# What is it?
Hex takes an `PNG` image and a corresponding file to recreate the image by replacing all pixels with colored hex values. I wanted to put up some art for my place and thought it would be fun to blend it with a programmers prospective. The output of the file is a `postscript` file.

# Input
`FILE` = Anything - the program just takes the hex values from it

`IMAGE` = Tried with PNG files. JPEG files should work but the algorithm takes into factor the alpha channel so all corresponding lines of code will need to be commented out

# Examples

<p align="center">
  <img src="https://github.com/sacert/Hex/blob/master/examples/link.png" alt="Screen shot 1" width="250"/>
  <img src="https://github.com/sacert/Hex/blob/master/examples/tardis.png" alt="Screen shot 2" width="250"/>
</p>

For **Toon Link**:

`FILE` = Legend of Zelda: Breath of the Wild theme song (mp3)

For **Tardis**

`FILE` = Doctor Who Theme song (mp3)


<p align="center">
  <img src="https://github.com/sacert/Hex/blob/master/examples/link_zoon.png" alt="Screen shot 1" width="400"/>
</p>
Here it is shown how each "pixel" of the image is simply a colored hex value.


# Getting Start
Within the python file are 4 globals, set these accordingly:

```
FONT_SIZE = 4               # Pixel size
FILE_NAME = "input.mp3"     # Name of file to get hex values from
IMAGE_NAME = "input.png"    # Name of image file
DATA_OFFSET = 32            # Where to start reading data from (mp3 music data starts at 32 by)
```

# Dependencies
- Turtle
- Tkinter
- PIL


# Licensing 
MIT
