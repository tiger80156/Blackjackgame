from random import randint
from collections import namedtuple
Card = namedtuple("card",("rank","suit"))
ranks = [n for n in range(1,14)]
suits = [n for n in range(2,11)]+list("AJQK")

class gameplay:
    
    def __init__(self):
        self._card = [Card(rank,suit) for rank in ranks for suit in suits]
        self._money = 1000
        for i in range(13):
            self.card.append(0)
        self.player_num = 0
        self.dealer_num = 0
        self.betting_money = 0
        
    def game_start(self, game_start):
        
        if game_start is 'y':
            print("*********game started*********")
            print("The buck you have: {} ".format(self.money))
            while True:
                self.betting_money = input("Entry the amount you want to bit: ")
    
                try:
                    self.betting_money = int(self.betting_money)
                    if self.betting_money <= self.money:
                        self.money = self.money - self.betting_money
                        return True
                    else:
                        return False
            
                except:
                    print("Pleas entry a number")
        return False

    
    def draw_card(self, drawer):
        while True:
            rand = randint(0,12)
            if  self.card[rand] < 4:
                if drawer is 1:
                    if rand <= 10 :
                        self.player_num = self.player_num + rand + 1
                    elif rand >= 10:
                        self.player_num = self.player_num + 10 
                    result = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
                    print("You get {}".format(result[rand]))
                  
                else:
                    self.dealer_num = self.dealer_num + rand +1
                self.card[rand] = self.card[rand] + 1 
                break
        
    def verify(self):
        while self.player_num >= self.dealer_num:
            self.draw_card(2)
        
        print("The dealer number is {}".format(self.dealer_num))
        if self.dealer_num > 21:
            print("You win")
            self.money = self.money + 2*self.betting_money
            self.reset_game()
        
        else: 
            print("You loss")
            self.dealer_num = 0
            self.player_num = 0
            self.reset_game()
    
    def reset_game(self):
        self.dealer_num = 0
        self.player_num = 0

