from PIL import Image

path="./images/nevsky.jfif"
myImg = Image.open(path)

dimentionX = int(myImg.height / 3)
dimentionY = int(myImg.width / 3)
resizedImage = myImg.resize((dimentionX, dimentionY))
resizedImage.save("./images/resized_image.png")
resizedImage.show()

flippedLeftRightImage = myImg.transpose(Image.FLIP_LEFT_RIGHT)
flippedLeftRightImage.save("./images/flipped_left_right.png")
flippedLeftRightImage.show()

flippedTopBottomImage = myImg.transpose(Image.FLIP_TOP_BOTTOM)
flippedTopBottomImage.save("./images/flipped_top_bottom.png")
flippedTopBottomImage.show()