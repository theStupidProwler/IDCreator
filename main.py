from random import randrange
import sys
def readAssets(typeOfAssets):
    global language
    fileName = "assets/"+ language + "/" + typeOfAssets + ".txt"
    asset = open(fileName, 'r')
    listing = []
    listing = asset.readlines()
    return listing
def parseArgs():
    global gender, minAge, maxAge, language
    inc = 0
    if(len(sys.argv) == 1):
        return
    while(inc < len(sys.argv)):
        if(sys.argv[inc] == "-g"):
            inc = inc + 1
            gender = sys.argv[inc].upper()
        else:
            if(randrange(0,2) == 1):
                gender = "F"
            else:
                gender = "M"
        if(sys.argv[inc] == "-l"):
            inc = inc + 1
            language = sys.argv[inc].lower()
        if(sys.argv[inc] == "-a"):
            inc = inc + 1
            minNMax = sys.argv[inc]
            minNMax = minNMax.split('-')
            minAge = int(minNMax[0])
            maxAge = int(minNMax[1]) + 1
        inc = inc + 1
def age():
    global minAge, maxAge
    return randrange(minAge, maxAge)
global language
parseArgs()
inc = 0
listNames = readAssets("familyNames")
listFirstNames = readAssets("firstNames"+ gender)
print("First Name:",end="")
print(listFirstNames[randrange(0,randrange(0,len(listFirstNames)))])
print("Family Name:",end="")
print(listNames[randrange(0,len(listNames))])
print("Age:",end="")
print(age())
