#================================= Tutorial link
#https://pillow.readthedocs.io/en/stable/

from PIL import Image

#==================================================================== we must firstly open the image

#here I used relative path, but we can use the absolute if the image is saved in another folder
path = "./images/image.jfif"
# newPath = "./images/new.png"
myImg = Image.open(path)
# newImg = Image.open(newPath)
# print(newImg)
# newImg.show()
# myImg.show()
# print(myImg)
# myImg.save("new.png")
# myNewImg = Image.open("./images/")
#===================================================================== Crop image 

# myBox = (50,50,100,100) #top left right buttom
# mynewImage = myImg.crop(myBox)
# mynewImage.show()

#==================================================================== Convert image

# myConvertedImage = myImg.convert("L")
# myConvertedImage.show()


#==================================================================  the file contents

# print(myImg) # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=225x225 at 0x1E657A85E80>

# print(myImg.format)

# print(myImg.size)

# print(myImg.mode)

#==================================================================  change img dimentions

# newSecImg = myImg.resize((100,100))
# newSecImg.show()

# imgSize = myImg.size
# dimentionX = int(imgSize[0] / 3)
# dimentionY = int(imgSize[1] / 3)
# print(type(dimentionX))
# print(dimentionY)

# smallImg = myImg.resize((dimentionX,dimentionY))
# smallImg.show()
# copyImg = myImg.copy()
# print(copyImg)
# copyImg.show()
# copyImg.thumbnail((100,20)) #20X20  because thumbnail method respect ratio
# copyImg.show()
# thumbImg = copyImg.thumbnail((100,200))
# thumbImg.show()
# print(thumbImg.size)

#==================================================================  Rortation

# rotatedImg = myImg.rotate(100.25) 
# rotatedImg.show()
# rotatedImg.save("rotated_img.png")

#==================================================================  transpose()

# myImg.show()
# rotatedImage = myImg.transpose(Image.TRANSVERSE)
# rotatedImage.show()

# flippedLeftRightImage = myImg.transpose(Image.FLIP_LEFT_RIGHT)
# flippedLeftRightImage.show()
# flippedTopBottomImage = myImg.transpose(Image.FLIP_TOP_BOTTOM)
# flippedTopBottomImage.show()


# Syntax
# Image.transpose(method)
# Image: Refers to the image object to which the transpose operations are to be applied.
# method: Specifies the type of transpose operation to perform. It can take one of the following values:
# Image.FLIP_LEFT_RIGHT: Flips the image horizontally (left to right).
# Image.FLIP_TOP_BOTTOM: Flips the image vertically (top to bottom).
# Image.ROTATE_90: Rotates the image by 90 degrees anticlockwise.
# Image.ROTATE_180: Rotates the image by 180 degrees.
# Image.ROTATE_270: Rotates the image by 270 degrees anticlockwise.
# Image.TRANSPOSE: Transposes the image, which swaps the image’s rows and columns.
# Image.TRANSVERSE: Performs a diagonal flip from the bottom-left to the top-right of the image.