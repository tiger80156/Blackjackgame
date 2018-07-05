from random import randint
from collections import namedtuple
from random import randint
from player import PlayerInfo

#Initialize
Card = namedtuple("card",("rank","suit"))
suits = ["HEART","Diamonds","Clovers","Spades"]
ranks = [n for n in range(2,11)]+list("AJQK")

class CardBox(PlayerInfo):
    
    def __init__(self,playerNumber):
        self._card = [Card(rank,suit) for rank in ranks 
                                    for suit in suits]
        self._money = dict(player=0,host=0)
        super().__init__(playerNumber)

        self._playerNow = 0

        self._allChips = 0

    def setPlayerNum(self,playerNow):
        self._playerNow = playerNow

    def choiceCard(self,chipNumber):
        # Get Two Card First
        for i in range(2):
            rni = randint(0,len(self._card)-1)
            chocar = self._card.pop(rni)
            self.addPoint(chocar[0],self._playerNow)
            print("The card you get is",chocar)
        print("Player{} point is {}".format(self._playerNow+1 , self._point[self._playerNow]))

        while True:
            draw = input("Hit for 'h' & Stand for 's' & break for anyother Key: ")        
                
            #Raond choice Card

            if draw == "s":
                return 0
            
            if draw == "h":

                print("The card you draw is",self.drawCard())
                print("Player{} point is".format(self._playerNow+1) , self._point[self._playerNow])

                
                # The point is greater than 21; Lose the game. Add all chips together.
                if self.checkPoint():
                    self._money[self._playerNow] -= chipNumber
                    self._allChips = chipNumber
                    print("The player{} chip now is : {}".format(self._playerNow+1,self._money[self._playerNow])) 
                    break
            
            else:
                return "b"

    # Check the player point 
    def checkPoint(self):
        # The point bigger than 21 return True to minus drawer point
        if self._point[self._playerNow] > 21:
            print("You are lose !")
            return True
        
        return False

    #Check who is winner
    def checkWinner(self):

        maxNum = 0
        winner = None
        
        # Find the winner who point is between 21 - 0
        for i in range(len(self._point)):
            item = self._point.pop()
            if 21 - item > maxNum:
                maxNum = 21 - item
                winner = i
        
        # If this game have winner go to bonus section 
        if winner:
            # The bonus section is compare the number with host
            self.bonus(maxNum,winner)
            print("The winner is {}".format(winner+1))
            self._money[i] +=  self._allChips


    #Compare the host number and winner Number
    def bonus(self,winnerNum,winnerPlayer):
        hostPoint = 0

        while hostPoint < winnerNum:
            rni = randint(0,len(self._card)-1)
            chocar = self._card.pop(rni)
            print("Host card is {}".format(chocar[0]))

            if chocar[0] in range(2,10): 
                hostPoint += chocar[0]
            elif chocar[0] == 'A':
                hostPoint += 1
            else:
                hostPoint += 10

            # When host lose the game, give winner extra number  
            if hostPoint > 21:
                self._money[winnerPlayer] += self._allChips
                break
        
        # else:
        #     self.addPoint(self._allChips,winnerPlayer)
            


    def drawCard(self):
        rni = randint(0,len(self._card)-1)
        chocar = self._card.pop(rni)
        self.addPoint(chocar[0],self._playerNow)
        return chocar
