import pprint
import re
import glob
import os
import os.path
import sys




entry = "singvolna02-174" # add the appropriate path to  the -CAT files
filename = "%s-CAT.txt" % (entry)
#FILE = open(filename)
#lines = FILE.readlines()
#FILE.close()

# trains a model of all syntactic categories based off of -categories files

def modelMaker(file, categoryFSAs):
    F = open(file)
    lines = F.readlines()
    F.close()
    for line in lines:
        if len(line) >= 2:
            parts = line.split("\t")
            if parts[0] not in categoryFSAs.keys():
                categoryFSAs[parts[0]] = {}
            tempTags = categoryFSAs.get(parts[0])
            POStags = parts[1:]
            pprint.pprint(POStags)
            while len(POStags) > 0:
                if POStags[0] not in tempTags.keys():
                    tempTags[POStags[0]] = {}
                pprint.pprint(POStags)
                POStags.pop()
                # reinitialize tempTags to its place in categoryFSAs
                tempTags = tempTags.get(POStags[0])
    return categoryFSAs

FSA = {}
for f in os.listdir(os.getcwd()):
    if f != (entry + ".txt"):
        FSA = modelMaker(f, FSA)

outputname = "%s-mTRAIN.txt" % entry
OUTPUT = open(outputname, "w")

pprint.pprint(FSA)
