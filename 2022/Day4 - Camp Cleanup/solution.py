# Settings
inputPath = r'C:/Github-Projects/AdventOfCode/2022/Day4 - Camp Cleanup/input.in'

def comparePairs(firstPairRange: list[int], SecondPairRange: list[int]):
    maxFirstPair = firstPairRange[firstPairRange.index(max(firstPairRange))]
    minFirstPair = firstPairRange[firstPairRange.index(min(firstPairRange))]
    
    maxSecondPair = SecondPairRange[SecondPairRange.index(max(SecondPairRange))]
    minSecondPair = SecondPairRange[SecondPairRange.index(min(SecondPairRange))]

    if (maxFirstPair >= maxSecondPair and minFirstPair <= minSecondPair):
        print ("includes")
        return 1
    if (maxSecondPair >= maxFirstPair and minSecondPair <= minFirstPair):
        print ("includes")
        return 1
    return 0

with open(inputPath, 'r', encoding="utf-8") as file:
    lines = file.readlines()
    counter = 0
    for line in lines:
        line.strip()
        print("--- Pairs:",line, "---")

        sectionRange = line.strip().split(",")
        firstPairRange = sectionRange[0].strip().split("-")
        SecondPairRange = sectionRange[1].strip().split("-")

        #Convert to int
        firstPairRange = list(map(int, firstPairRange))
        SecondPairRange = list(map(int, SecondPairRange))

        counter = counter + comparePairs(firstPairRange, SecondPairRange)
        print("--- Line-End ---")
    print("Counted Pairs:",counter)