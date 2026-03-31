from PIL import Image


#============================= Open the image 
path = "./images/image.jfif"
myImg = Image.open(path)

#============================= Show the image 
myImg.show()

#============================= Show the image info
imgSize = myImg.size
imgFormat = myImg.format
imgMode  = myImg.mode

print(f"This image has size: {imgSize}, its format: {imgFormat}, its color mode: {imgMode} ")