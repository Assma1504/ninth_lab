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


