# Settings
inputPath = r'C:/Github-Projects/AdventOfCode/2022/Day3 - Rucksack Reorganization/input.in'

foundLetters = []

def compare(str1, str2, str3):
    foundLetters = []
    i = 0
    points = 0
    print("String1", str1, "String2", str2, "String3", str3)
    while i < len(str1):
        if str1[i] in str2 and str1[i] not in foundLetters:
            if str1[i] in str3:
                print("Found letter: ", str1[i])
                foundLetters.append(str1[i])
                points += getPointsForLetter(str1[i])
        i += 1
    print(foundLetters)
    return points

def getPointsForLetter(char):
    points = 0
    idOfLetter = 0
    
    if char.islower():
        idOfLetter = ord(char) - 96
    
    if char.isupper():
        idOfLetter = ord(char.lower()) - 96 +26
    
    points = points + idOfLetter
    print("Char", char, ":", idOfLetter, "points")
    
    return points

with open(inputPath, 'r', encoding="utf-8") as file:
    lines = file.readlines()

    itemsInARucksack = 3
    startAtLine = 0
    endAtLine = itemsInARucksack

    points = 0

    i = 0
    while i < len(lines)/itemsInARucksack:
        arr = lines[startAtLine:endAtLine]
        points += compare(arr[0].strip(), arr[1].strip(), arr[2].strip())
        i += 1
        startAtLine += itemsInARucksack
        endAtLine += itemsInARucksack
    print ("Total points:",points)

