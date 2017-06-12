from random import randrange
def readAssets(typeOfAssets):
    fileName = "assets/" + typeOfAssets + ".txt"
    asset = open(fileName, 'r')
    listing = []
    listing = asset.readlines()
    return listing
gender = "M"
inc = 0
listNames = readAssets("familyNames")
listFirstNames = readAssets("firstNames"+ gender)
print(listNames[randrange(0,len(listNames))])
