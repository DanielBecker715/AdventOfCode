# Settings
inputPath = r'C:/Github-Projects/AdventOfCode/2022/Day1 - Calorie Counting/input.txt'

elfCounter = 0
arr = []

with open(inputPath, 'r', encoding="utf-8") as file:
    lines = file.readlines()

    elfCalories = 0

    for line in lines:
        if line.strip():
            #Line is not empty
            elfCalories = elfCalories + int(line)
        else:            
            # Line is empty
            print("Elf: ", elfCounter+1)
            arr.append(elfCalories)
            print("Calories: ", arr[elfCounter])
            
            elfCounter=elfCounter+1
            elfCalories = 0

    print("The highest elf:", arr.index(max(arr))+1, "has", max(arr),"cal")

    arr.sort(reverse=True)

    caloriesOfTopElfs = 0
    numberOfTopElfs = 3
    for i in range(numberOfTopElfs):
        caloriesOfTopElfs = caloriesOfTopElfs + arr[i]
        print("The", arr.index(arr[i])+1, "highest elf has ", arr[i],"cal")
    print("The top", numberOfTopElfs, "have a total of", caloriesOfTopElfs,"cal")