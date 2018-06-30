from collections import namedtuple

class PlayerInfo():
    def __init__(self,playerNumber):
        self._money = [1000 for i in range(playerNumber)]
        self._point = [0 for i in range(playerNumber)]

    def __getattr__(self,name):
        if name == "money":
            return self._money
        elif name == "point":
            return self._point

    def addPoint(self,pointDraw,playerNum):
        if pointDraw in range(2,10):
            self._point[playerNum] += pointDraw
        elif pointDraw == "A":
            self._point[playerNum] += 1
        else:
            self._point[playerNum] += 10

