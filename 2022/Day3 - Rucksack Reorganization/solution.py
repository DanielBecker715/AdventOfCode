# Settings
inputPath = r'C:/Github-Projects/AdventOfCode/2022/Day3 - Rucksack Reorganization/input.in'

foundLetters = []
points = 0

def compare(str1, str2):
    i = 0
    while i < len(str1):
        if str1[i] in str2:
            foundLetters.append(str1[i])
            break
        i += 1

with open(inputPath, 'r', encoding="utf-8") as file:
    lines = file.readlines()

    for line in lines:
        length = len(line)
        firstHalf = line[0:length//2]
        SecondHalf = line[length//2:]
        print("String:", firstHalf, "|", SecondHalf)
        compare(firstHalf, SecondHalf)

    print("Found:",foundLetters)
    for char in foundLetters:
        if char.islower():
            idOfLetter = ord(char) - 96
            points += idOfLetter
            print("Char", char, ":", idOfLetter, "points")
        if char.isupper():
            idOfLetter = ord(char.lower()) - 96 +26
            points += idOfLetter
            print("Char", char, ":", idOfLetter, "points")
    print ("Total points:",points)

