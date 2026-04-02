from PIL import Image, ImageFont, ImageDraw


listPath = ["./images/filters/1.jfif", "./images/filters/2.jfif","./images/filters/3.jfif","./images/filters/4.jfif","./images/filters/5.jfif"]
listImages = [Image.open(path) for path in listPath]
myRange = range(5)
counter = 1

for i in myRange:
    heightWaterMark = int(listImages[i].height / 4)
    widthWaterMark = int(listImages[i].width / 4)
    newImg = Image.new("RGBA", listImages[i].size)
    imgDraw = ImageDraw.Draw(newImg)
    waterMark = "Assma"
    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", size = 50)
    imgDraw.text((heightWaterMark,widthWaterMark), waterMark, font = font, fill = (200,200,200,100))
    listImages[i].paste(newImg, newImg)
    listImages[i].show()
    listImages[i].save(f"./images/filters/imageWithWaterMark{counter}.png")
    counter += 1
    print(newImg)








# path="./images/8.jfif"
# myImg = Image.open(path)
# newImg = Image.new("RGBA", myImg.size)
# heightWaterMark = int(myImg.height / 4)
# widthWaterMark = int(myImg.width / 4)
# imgDraw = ImageDraw.Draw(newImg)
# waterMark = "Assma"
# font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", size = 50)
# imgDraw.text((heightWaterMark,widthWaterMark), waterMark, font = font, fill = (200,200,200,100))

# myImg.paste(newImg, newImg)
# myImg.show()