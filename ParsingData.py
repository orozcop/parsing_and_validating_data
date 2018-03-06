
import ModuleForAssignment
import re
import csv

dirtyNamesCsv = open("10000DirtyNames.csv", "r")

tempData = dirtyNamesCsv.read()
numberOfCharacters = ModuleForAssignment.countCharacters(tempData) #Module used to interpret the number of characters in the file.
                                                                   #This could be done simply in the same project but I wanted to experiment working with a module.

dirtyNamesCsv.close()


AllNamesList = []
CleanNamesList = []
InvalidNamesList = []
HyphenNamesList = []
tempCell = ""

tempData = tempData + "," #adds a comma at the end of string so that the for
                          #loop shown next doesn't discard the last item.

for char in tempData:
    if "," in char:
        AllNamesList.append(tempCell) #load into a list, every string from a column/between commas.
        tempCell = ""
    else:
        tempCell = tempCell + char


pattern = "^[A-Za-z]+[-]?[A-Za-z]+"
inputString = AllNamesList[521]

for name in AllNamesList:
    if re.match(pattern, name) != None:
        name = str.title(name) #used to capitalise every word
        CleanNamesList.append(name)
    else:
        InvalidNamesList.append(name)

with open("CleanNames.csv", "w") as CleanNamesCsv:
    CleanNamesCsv.write(','.join(CleanNamesList))

with open("InvalidNames.csv", "w") as InvalidNamesCsv:
    InvalidNamesCsv.write(','.join(InvalidNamesList))
