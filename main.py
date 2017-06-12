from random import randrange
import sys
def readAssets(typeOfAssets):
    fileName = "assets/" + typeOfAssets + ".txt"
    asset = open(fileName, 'r')
    listing = []
    listing = asset.readlines()
    return listing
def parseArgs(): #getopt is for fags
    global gender
    inc = 0
    if(len(sys.argv) == 1):
        return
    while(inc < len(sys.argv)):
        if(sys.argv[inc] == "-g"):
            inc = inc + 1
            gender = sys.argv[inc].upper()
        inc = inc + 1
def age():
    return randrange(randrange(1,16),randrange(50,80))
global gender
parseArgs()
inc = 0
listNames = readAssets("familyNames")
listFirstNames = readAssets("firstNames"+ gender)
print(listFirstNames[randrange(0,randrange(0,len(listFirstNames)))])
print(listNames[randrange(0,len(listNames))])
print(age())
