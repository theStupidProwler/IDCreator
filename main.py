from random import randrange
import sys

class Character:
    def __init__(self):
        self.firstName = ""
        self.familyName = ""
        self.city = ""
        self.age = ""
        self.job = ""
        self.gender = "M"

    def randomGender(self):
        if(randrange(0,2) == 1):
            self.gender = "F" #did u just assume mine
        else:
            self.gender = "M"

    def defineFamilyName(self):
        listNames = readAssets("familyNames")
        self.familyName = listNames[randrange(0,len(listNames))].title()

    def defineFirstName(self):
        global language
        typeOfAssets = "firstNames"+ self.gender
        listFirstNames = readAssets(typeOfAssets)
        self.firstName = listFirstNames[randrange(0,randrange(1,randrange(2,randrange(3,len(listFirstNames)))))].title()

    def defineJob(self):
        if(self.age > 16):
            listMetiers = readAssets("jobNames")
            if(randrange(0,11) == "1"):
                self.job = listMetiers[0].title()
            if(self.age < 25 & randrange(1,self.age)< 15):
                self.job = listMetiers[1].title()
            self.job = listMetiers[randrange(1, len(listMetiers))].title()

    def defineCity(self):
        listCity = readAssets("cityNames")
        self.city = listCity[randrange(0,randrange(1,len(listCity)))]

    def defineAge(self, minAge, maxAge):
        self.age = randrange(minAge, maxAge)

def readAssets(typeOfAssets):
    global language
    fileName = "assets/"+ language + "/" + typeOfAssets + ".txt"
    asset = open(fileName, 'r')
    listing = []
    listing = asset.readlines()
    return listing

def parseArgs():
    global language
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
            mainCharacter.gender = True
            inc = inc + 1
            mainCharacter.gender = sys.argv[inc].upper()
        elif(hasGender == False):
            mainCharacter.randomGender()
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
            mainCharacter.defineAge(minAge, maxAge)
        elif(hasAge== False):
            minAge = 1
            maxAge = 115
            mainCharacter.defineAge(minAge, maxAge)
        inc = inc + 1
def defineMainCharacter():
    mainCharacter.defineFirstName()
    mainCharacter.defineFamilyName()
    mainCharacter.defineJob()
    mainCharacter.defineCity()


mainCharacter = Character()
parseArgs()
defineMainCharacter()
inc = 0
print("\nFirst Name:", mainCharacter.firstName)
print("Family Name:",mainCharacter.familyName)
print("Age:",mainCharacter.age)
print("\nJob:",mainCharacter.job)
print("City:",mainCharacter.city)
