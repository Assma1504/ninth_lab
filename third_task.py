from PIL import Image, ImageFilter
listPath = ["./images/filters/1.jfif", "./images/filters/2.jfif","./images/filters/3.jfif","./images/filters/4.jfif","./images/filters/5.jfif"]
listImages = [Image.open(path) for path in listPath]
listFilters= ["BLUR","CONTOUR","DETAIL","EDGE_ENHANCE","EDGE_ENHANCE_MORE","EMBOSS","FIND_EDGES","SHARPEN","SMOOTH","SMOOTH_MORE"]
myRange = range(5)

# for i in myRange:
#     filtredImage = listImages[i].filter(ImageFilter.CONTOUR)
#     # filtredImage.show()
#     newName = listPath[i].split("/")[-1]
#     filtredImage.save(f"./images/filters/filtredImage{newName}")


#============================ Other Option =================
# I want to ask user firstly to choose an image and then then choose the filter that he wants to apply and finally chhose a name for the image

numberImg = input("Please choose a number from 1 to 5: ")
while int(numberImg)< 1 or int(numberImg)> 5:
    print("Please choose a correct number from 1 to 5")
    numberImg = input("Please choose a number from 1 to 5: ")

filterNumber =int(input("Please choose a filter from the list (just the number): \n 1: BLUR \n 2:CONTOUR \n 3:DETAIL \n 4:EDGE_ENHANCE \n 5:EDGE_ENHANCE_MORE \n 6:EMBOSS \n 7:FIND_EDGES \n 8:SHARPEN \n 9:SMOOTH  \n 10:SMOOTH_MORE \n"))
while int(filterNumber)< 1 or int(filterNumber)> 10:
    print("Please choose a correct number from 1 to 10")
    filterNumber =int(input("Please choose a filter from the list (just the number): \n 1: BLUR \n 2:CONTOUR \n 3:DETAIL \n 4:EDGE_ENHANCE \n 5:EDGE_ENHANCE_MORE \n 6:EMBOSS \n 7:FIND_EDGES \n 8:SHARPEN \n 9:SMOOTH  \n 10:SMOOTH_MORE \n"))
else:
    pathImage = (f"./images/filters/{numberImg}.jfif") 
    userImage = Image.open(pathImage)
    filterName = listFilters[filterNumber-1]
    actualFilter = getattr(ImageFilter, filterName)
    filterdImage = userImage.filter(actualFilter)
    # filterdImage.show()


imageName = input("Your Image is ready, you need just to choose a name for your new image: ")
filterdImage.save(f"./images/filters/{imageName}.jpg")




