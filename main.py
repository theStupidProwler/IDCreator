def readAssets(typeOfAssets):
    fileName = "assets/" + typeOfAssets + ".txt"
    asset = open(fileName, 'r')
    lineContent = asset.read()
    listing = []
    listing.append(lineContent)
    inc = 0
    while(lineContent):
        inc = inc + 1
        listing.append(lineContent)
        lineContent = asset.read()
    return listing
inc = 0
listAsf = readAssets("familyNames")
while(listAsf[inc]):
    print(listAsf[inc])
    inc = inc + 1
