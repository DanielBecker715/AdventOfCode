# Settings
inputPath = r'C:/Github-Projects/AdventOfCode/2022/Day2 - Rock Paper Scissors/input.txt'
wonMessage = "Result: WIN!"
drawMessage = "Result: It's a draw, both won!"
defeatMessage = "Result: Defeat!"

#Default Points
points = 0

#Standard values during an event
pointsByWin = 6
pointsByDraw = 3
pointsByDefeat = 0

#Points for playing with:
pointsByRock = 1
pointsByPaper = 2
pointsByScissor = 3

gameCounter = 1

with open(inputPath, 'r', encoding="utf-8") as file:
    lines = file.readlines()

    for line in lines:
        print("----- Game: ", gameCounter, "-----")

        choices = line.split()

        match choices[0]:
            case "A":
                print("Opponent choose rock")
                opponentsChoice = "rock"
            case "B":
                print("Opponent choose paper")
                opponentsChoice = "paper"
            case "C":
                print("Opponent choose scissor")
                opponentsChoice = "scissor"

        match choices[1]:
            case "X":
                print("I choose rock")
                myChoice = "rock"
                points = points + pointsByRock
            case "Y":
                print("I choose paper")
                myChoice = "paper"
                points = points + pointsByPaper
            case "Z":
                print("I choose scissor")
                myChoice = "scissor"
                points = points + pointsByScissor

        
        if (opponentsChoice == myChoice):
            print(drawMessage)
            points = points + 3
        else:
            match opponentsChoice:
                case "rock":
                    if (myChoice in ["paper"]):
                        print(wonMessage, myChoice, "beats", opponentsChoice)
                        points = points + pointsByWin
                    else:
                        print(defeatMessage, opponentsChoice, "beats", myChoice)
                        points = points + pointsByDefeat
                case "paper":
                    if (myChoice in ["scissor"]):
                        print(wonMessage, myChoice, "beats", opponentsChoice)
                        points = points + pointsByWin
                    else:
                        print(defeatMessage, opponentsChoice, "beats", myChoice)
                        points = points + pointsByDefeat
                case "scissor":
                    if (myChoice in ["rock"]):
                        print(wonMessage, myChoice, "beats", opponentsChoice)
                        points = points + pointsByWin
                    else:
                        print(defeatMessage, opponentsChoice, "beats", myChoice)
                        points = points + pointsByDefeat              

        gameCounter = gameCounter + 1
        print ("Current points: ", points)
    print ("Your total earned points:", points)