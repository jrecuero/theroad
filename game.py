import player
from roadCollections import basicRoad


class Game(object):

    def __init__(self, theNbrOfPlayers=3):
        self._road = None
        self._players = []
        self._nbfOfPlayers = theNbrOfPlayers

    @property
    def Road(self):
        return self._road

    @Road.setter
    def Road(self, theRoad):
        self._road = theRoad

    def getPlayer(self, theIndex):
        return self._players[theIndex]

    def _createPlayers(self):
        for i in range(self._nbfOfPlayers):
            p = player.Player('player{0}'.format(i))
            p.init()
            self._players.append(p)

    def roll(self, thePlayer):
        pos = thePlayer.Pos
        index, _ = self.Road.segmentAt(pos)
        segment = self.Road[index]
        g = segment.Gear
        return thePlayer.roll(g)

    def move(self, thePlayer):
        pos = self.roll().Value
        thePlayer.Pos += pos
        return thePlayer.Pos

    def init(self):
        self._createPlayers()
        self.Road = basicRoad()
