class board:
    def __init__(self):
        self.places = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        self.turn = "You"
        self.lastenemypocket = 0
        self.lastmypocket = 0


    def getpocket(self, n):
        return self.places[n]





    def move(self,n):
        self.turn = "Enemy"
        currentamount = self.places[n]
        self.places[n] = 0
        currentplace = n
        #print(currentamount, "is the currrentamount")
        while currentamount > 0:
            currentplace = currentplace+1
            if currentplace == 13:
                currentplace = 0




            if currentamount == 1 and self.places[currentplace] == 0 and currentplace != 6:

                offset = 6-currentplace
                previousscore = self.places[6]
                self.places[6] = self.places[6+offset]+self.places[6]

                self.places[offset+6] = 0

            if currentamount == 1 and currentplace == 6:
                self.turn = "You"
            self.places[currentplace] = self.places[currentplace] + 1
            currentamount = currentamount - 1


    def enemymove(self,n):
        n = 12-n
        self.turn = "You"
        print("Enemy move starting")

        currentamount = self.places[n]
        self.places[n] = 0
        currentplace = n
        while currentamount > 0:
            print("currennt amount in hand: ", currentamount)
            currentplace = currentplace+1
            if currentplace > 13:
                currentplace = 0

            if currentplace == 6:
                currentplace = 7



            if currentamount == 1 and self.places[currentplace] == 0:
                print("only hand one in hand and place is empty")
                if currentplace == 13:
                    self.turn = "Enemy"
                offset = 12 - currentplace
                self.places[13] = self.places[offset] + self.places[13]
                print("itt vagyok ", currentplace,"az offsetem ", offset)
                self.places[offset] = 0

            if currentamount == 1 and currentplace == 13:
                self.turn = "Enemy"
            self.places[currentplace] = self.places[currentplace] + 1
            currentamount = currentamount - 1


    def getsteal(self,n):

        offset = 6-n

        return self.places[6+offset]




