import pprint
import re

entry = "studymh2-0197"
filename = "%s.txt" % (entry)
FILE = open(filename)
lines = FILE.readlines()
FILE.close()

outputname = "%s-PARSE.txt" % entry
OUTPUT = open(outputname, "w")

def parse(lines):
    final_output = []
    singletonString = ""
    for line in lines:
        line = line.strip()
        if len(line) > 0 and line[0] != ";":
            for x in range(len(line)):
                if ord(line[x]) > 127:
                    line = line.replace(line[x], " ")
            singletonString += line
        if len(line) == 0:
            if len(singletonString) > 0:
                editedSS = re.sub(r'[ a-z+/+\+]', "", singletonString)
                editedSS = re.sub(r'\.', '.sf', editedSS)
                editedSS = re.sub(r',', ',sp', editedSS)
                final_output.append(editedSS)
            print(editedSS + "\n")
            singletonString = ""

    for sentence in final_output:
        OUTPUT.write(sentence)
        OUTPUT.write("\n\n")

parse(lines)