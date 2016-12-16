import pprint
import re

entry = "studymh2-0197"
filename = "%s.txt" % (entry)
FILE = open(filename)
lines = FILE.readlines()
FILE.close()

outputname = "%s-BARE.txt" % entry
OUTPUT = open(outputname, "w")

def makeBare(lines):
    newLines = []
    newResult = []
    for line in lines:
        line = line.strip()
        for x in range(len(line)):
            if ord(line[x]) > 127:
                line = line.replace(line[x], "H")
            line = line.replace("("," ")
            line = line.replace(")"," ")
        line = line.strip()
        if len(line) > 0 and line[0] == ";":
            newLines.append(newResult)
            newResult = []
        elif "H" in line:
            while "P" in line or "V" in line:
                if "P" in line:
                    PVal = line.index("P")
                elif "V" in line:
                    PVal = line.index("V")
                line = line[PVal + 2:]
            line = line.replace("H", "")
            line = line.replace("/", "")
            line = line.strip()
            line = line.split("+")
            for x in range(len(line)):
                entry = line[x].strip()
                line[x] = entry
            newResult.append(line)

    for sentence in newLines:
        for word in sentence:
            for POS in word:
                OUTPUT.write(POS + "\t")
            OUTPUT.write("\n")
        OUTPUT.write("\n")

makeBare(lines)