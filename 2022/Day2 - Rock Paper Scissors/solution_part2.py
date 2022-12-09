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

    loseAgainstStone = "scissor"
    loseAgainstPaper = "rock"
    loseAgainstScissor = "paper"

    winAgainstStone = "paper"
    winAgainstPaper = "scissor"
    winAgainstScissor = "rock"

    for line in lines:
        print("----- Game: ", gameCounter, "-----")

        myChoice = ""
        choices = line.split()
        match choices[0]:
            case "A":
                opponentsChoice = "rock"
                print("Opponent choose rock")
                match choices[1]:
                    case "X":
                        myChoice = loseAgainstStone
                    case "Y":
                        myChoice = opponentsChoice
                    case "Z":
                        myChoice = winAgainstStone
                print("I choose", myChoice)
            case "B":
                opponentsChoice = "paper"
                print("Opponent choose paper")
                match choices[1]:
                    case "X":
                        myChoice = loseAgainstPaper
                    case "Y":
                        myChoice = opponentsChoice
                    case "Z":
                        myChoice = winAgainstPaper
                print("I choose", myChoice)
            case "C":
                opponentsChoice = "scissor"
                print("Opponent choose scissor")
                match choices[1]:
                    case "X":
                        myChoice = loseAgainstScissor
                    case "Y":
                        myChoice = opponentsChoice
                    case "Z":
                        myChoice = winAgainstScissor
                print("I choose", myChoice)

        if (myChoice == "rock"):
            points = points + 1
        if (myChoice == "paper"):
            points = points + 2
        if (myChoice == "scissor"):
            points = points + 3

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