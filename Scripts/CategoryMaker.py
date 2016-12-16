import pprint
import re

entry = "singvolna02-174"
filename = "%s.txt" % (entry)
FILE = open(filename)
lines = FILE.readlines()
FILE.close()

outputname = "%s-CAT.txt" % entry
OUTPUT = open(outputname, "w")

def makeBare(lines):
    newLines = []
    newResult = []
    for line in lines:
        line = line.strip()
        for x in range(len(line)):
            if ord(line[x]) > 127:
                line = line.replace(line[x], "H")

        if "H" in line and ";" not in line:
            newLines.append(line)
        elif len(line) == 0:
            newLines.append("\n")

    returnableLines = []
    for line in newLines:
        newL = re.sub(r"H+/", "", line)
        newL = re.sub(r"/", "", newL)
        newL = re.sub(r"\([A-Z+] \(", "(", newL)
        newL = re.sub(r"\(", "", newL)
        newL = re.sub(r"\)+", "", newL)
        returnableLines.append(newL)

    listOfCategories = []
    for line in returnableLines:
        preCategory = line.split()
        #pprint.pprint(preCategory)

        if len(preCategory) > 1:
            category = []
            category.append(preCategory[0])
            postCategory = preCategory[1].split("+")
            #pprint.pprint(postCategory)
            for cat in postCategory:
                category.append(cat)
            listOfCategories.append(category)

    for category in listOfCategories:
        #pprint.pprint(category)
        out = ""
        for word in category:
            out += word + "\t"
        OUTPUT.write(out)
        OUTPUT.write("\n")

makeBare(lines)