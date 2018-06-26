from random import randint
from collections import namedtuple
Card = namedtuple("card",("rank","suit"))
ranks = [n for n in range(1,14)]
suits = [n for n in range(2,11)]+list("AJQK")

class Player:
    
    def __init__:
        self._card = [Card(rank,suit) for rank in ranks for suit in suits]
        self._money = dict(player=0,host=0)

    