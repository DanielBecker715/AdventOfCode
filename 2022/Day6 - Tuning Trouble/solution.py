# Settings
inputPath = r'C:/Github-Projects/AdventOfCode/2022/Day6 - Tuning Trouble/input.in'

with open(inputPath, 'r', encoding="utf-8") as file:
    data = file.read()

p1 = False
p2 = False

for i in range(4, len(data)):
    part1 = set(data[(i-4):i])
    part2 = set(data[(i-14):i])
    if (not p1 and len(part1) == 4):
        print("Part1: ",part1, i)
        p1 = True
    if (not p2 and len(part2) == 14):
        print("Part2: ",part2, i)
        p2 = True