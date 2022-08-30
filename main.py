from board import board
import copy

# Press the green button in the gutter to run the script.

def getboardstring():
    return "___                         ___\nI I-I"+str(myboard.getpocket(12)) +"I-I"+str(myboard.getpocket(11)) +"I-I"+str(myboard.getpocket(10)) +"I-I"+str(myboard.getpocket(9)) +"I-I"+str(myboard.getpocket(8)) +"I-I"+str(myboard.getpocket(7)) +"I-I I\nI"+str(myboard.getpocket(13)) +"I                         I"+str(myboard.getpocket(6)) +"I\nI I-I"+str(myboard.getpocket(0)) +"I-I"+str(myboard.getpocket(1)) +"I-I"+str(myboard.getpocket(2)) +"I-I"+str(myboard.getpocket(3)) +"I-I"+str(myboard.getpocket(4)) +"I-I"+str(myboard.getpocket(5)) +"I-I I"

def getidealpockets(currentboard):
    idealpockets = 0
    closestidealpocket = -1
    for x in range(0,6):
        if x == 0:
            desiredplace = currentboard.getpocket(x) + x
        else:
            desiredplace = currentboard.getpocket(x) + x
        if desiredplace == 6:
            closestidealpocket = x
            idealpockets = idealpockets + 1

    return idealpockets, closestidealpocket


def getenemyidealpockets(currentboard):
    idealpockets = 0

    for x in range(7,12):
        desiredplace = currentboard.getpocket(x) + x
        if desiredplace == 13:

            idealpockets = idealpockets + 1

    return idealpockets





def checkifscores(x):
    if x == 0:
        desiredplace = myboard.getpocket(x) + 1 #get back to check if this is right or not
    else:
        desiredplace = myboard.getpocket(x) + x
    if desiredplace > 6:
        return True
    else:
        return False



def getbestmove():
    beststeal = getbeststeal()
    if beststeal[1] >=3:
        print("the steal is more or equal to 3 so this seemed to be a good move")
        return beststeal[0]+1
    idealpockets = getidealpockets(myboard)
    if idealpockets[0] > 0:
        print("this was the closest ideal pocket ready to score")
        return idealpockets[1]+1

        #first value is the index of the pocket second value is the amount of ideal pockets on the board
    bestmove = (0,0)
    bestmovenum = 0
    for x in range(0,6): #This is where I left off these two for loops should be well spearated and not like this. This first for loop below is supposed to be the Bruteforcer

        currentboard = copy.deepcopy(myboard)
        currentboard.move(x)
        currentmove = getidealpockets(currentboard)
        if currentmove[0] > bestmove[0]:
            bestmove = currentmove
            bestmovenum = x

    if bestmove[0] > 0:
        print("Decided to chose this because this move would prepare the most ideal pockets actually: ", bestmove[0])
        return bestmovenum+1

    ruincount = 5
    lastruin = 0
    bestruinmove = 0
    while ruincount > -1:
        currentruinboard = copy.deepcopy(myboard)
        currentruin = getenemyidealpockets(currentruinboard) #3152
        currentruinboard.move(ruincount)
        if currentruin < lastruin:
            lastruin = currentruin
            bestruinmove = ruincount
        ruincount = ruincount - 1
    if lastruin > 0:
        print("Decided to chose this because this move seems to ruin the most enemy ideal pockets: ", lastruin)
        return bestruinmove



    count = 5
    while count > -1:
        if checkifscores(count):
            print("Decided to go with this because it gives you a score at least ")
            return count+1
        count = count - 1


    lastamount = 0
    lastmove = 0
    for lx in range(0,5):
        if lx > lastamount:
            lastmove = lx

    return lastmove







def getbeststeal():
    experimentalboard = myboard
    laststeal = -5
    bestsofar = -1
    for x in range(0,5): #changed 6 to 5

        if experimentalboard.getpocket(x) == 0:
            continue
        if x == 0:
            desiredplace = experimentalboard.getpocket(x)+x
        else:
            desiredplace = experimentalboard.getpocket(x)+x
            while desiredplace >=13:
                offset = desiredplace-13
                desiredplace = offset


        if experimentalboard.getpocket(desiredplace) == 0 and experimentalboard.getsteal(desiredplace)> laststeal and desiredplace < 6:
            print(x, desiredplace, experimentalboard.getsteal(desiredplace))
            laststeal = experimentalboard.getsteal(desiredplace)
            bestsofar = x


    return bestsofar, laststeal









places = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
myboard = board()

if __name__ == '__main__':
    previousboard = board()


    while True:


        if myboard.turn == "You":

            print(getboardstring())
            print("recommended move: ", getbestmove())

            answer = input("You: ")
            if answer == "prev":
                myboard = copy.deepcopy(previousboard)
            else:
                previousboard = copy.deepcopy(myboard)
                myboard.move(int(answer) - 1)





        else: #myboard.turn == "Enemy":

            print("  ")
            print("  ")
            print(getboardstring())
            print("  ")

            answer = input("Enemy: ")
            if answer == "prev":

                myboard = copy.deepcopy(previousboard)

            else:
                previousboard = copy.deepcopy(myboard)
                myboard.move(int(answer) - 1)










