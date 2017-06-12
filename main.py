from random import randrange
def readAssets(typeOfAssets):
    fileName = "assets/" + typeOfAssets + ".txt"
    asset = open(fileName, 'r')
    listing = []
    listing = asset.readlines()
    return listing
inc = 0
listAsf = readAssets("familyNames")
print(listAsf[randrange(0,len(listAsf))])
