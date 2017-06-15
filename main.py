from random import randrange
import sys

def mainCharacter():
    McFirstName = familyName()
    McFamilyName = firstName(McGender)
    McCity = city()
    McAge = age()
    McJob = job()

def randomGender():
    if(randrange(0,2) == 1):
        gender = "F" #did u just assume mine
    else:
        gender = "M"
return gender

def familyName():
    listNames = readAssets("familyNames")
    MCfamilyName =listNames[randrange(0,len(listNames))].title()

def firstName(gender):
    listFirstNames = readAssets("firstNames"+ gender)
    return listFirstNames[randrange(0,randrange(1,randrange(2,randrange(3,len(listFirstNames)))))].title()

def job():
    global age
    if(age > 16):
        listMetiers = readAssets("jobNames")
        if(randrange(0,11) == "1"):
            return listMetiers[0].title()
        if(age < 25 & randrange(1,age)< 15):
            return listMetiers[1].title()
        return listMetiers[randrange(1, len(listMetiers))].title()

def city():
    listCity = readAssets("cityNames")
    return listCity[randrange(0,randrange(0,len(listCity)))]

def age():
    global minAge, maxAge
    return randrange(minAge, maxAge)

def readAssets(typeOfAssets):
    global language
    fileName = "assets/"+ language + "/" + typeOfAssets + ".txt"
    asset = open(fileName, 'r')
    listing = []
    listing = asset.readlines()
    return listing

def parseArgs():
    global McGender, minAge, maxAge, language
    hasGender, hasAge, hasLanguage= False, False, False
    inc = 0
    while(inc < len(sys.argv)):
        if(sys.argv[inc] == "-h"):
            print("Usage:  main.py -g <genderType(M/F)> -a <AgeBetween(min-max)> -l <language>\n Ex: \n\tpython3.5 main.py "+
                "\n\tpython3.5 main.py -g M -a 1-10 -l fr"+
                "\n\tpython3.5 main.py -g F"+
                "\n\tpython3.5 main.py -a 12,19 -l en\n")
            print("IDENTITY GENERATION",#assassin
             " \n\t-g <genderType>: choose gender (random is default)\n", #there isn't male pangenderfluidqueer yet
            "\t-a <AgeBetween min-max>: an age between 1 and 115 is default\n",
            "\t-l <language>: fr or en, default is en\n")
            sys.exit("No argument found")
        if(sys.argv[inc] == "-g"):
            hasGender = True
            inc = inc + 1
            gender = sys.argv[inc].upper()
        elif(hasGender == False):
            McGender = randomGender

        if(sys.argv[inc] == "-l"):
            inc = inc + 1
            language = sys.argv[inc].lower()
            hasLanguage = True
        elif(hasLanguage== False):
            language = "en"
        if(sys.argv[inc] == "-a"):
            hasAge = True
            inc = inc + 1
            minNMax = sys.argv[inc]
            minNMax = minNMax.split('-')
            minAge = int(minNMax[0])
            maxAge = int(minNMax[1]) + 1
        elif(hasAge== False):
            minAge = 1
            maxAge = 115
        inc = inc + 1

global language
parseArgs()
inc = 0
print("\nFirst Name:", McFirstName)
print("Family Name:",McFamilyName)
print("Age:",McAge)
print("\nJob:",McJob)
print("City:",McCity)
