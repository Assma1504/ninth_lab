#================================= Tutorial link
#https://pillow.readthedocs.io/en/stable/

from PIL import Image

#==================================================================== we must firstly open the image

#here I used relative path, but we can use the absolute if the image is saved in another folder
path = "./images/image.jfif"
myImg = Image.open(path)
# myImg.show()

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

#================================================================== Convert files to JPEG 
