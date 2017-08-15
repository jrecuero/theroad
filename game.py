import player
from roadCollections import basicRoad
from roadHandler import RoadHandler


class Game(object):

    def __init__(self, theNbrOfPlayers=3):
        self._road = None
        self._players = []
        self._nbfOfPlayers = theNbrOfPlayers
        self._roadHandler = None

    @property
    def Road(self):
        return self._road

    @Road.setter
    def Road(self, theRoad):
        self._road = theRoad

    @property
    def RoadHandler(self):
        return self._roadHandler

    @RoadHandler.setter
    def RoadHandler(self, theRoadHandler):
        self._roadHandler = theRoadHandler

    @property
    def NbrOfPlayers(self):
        return self._nbfOfPlayers

    def getPlayer(self, theIndex):
        return self._players[theIndex]

    def _createPlayers(self):
        for i in range(self._nbfOfPlayers):
            p = player.Player('player{0}'.format(i), theUser=True if i == 0 else False)
            p.init()
            self._players.append(p)

    def roll(self, thePlayer):
        pos = thePlayer.Pos
        segment = self.Road[pos]
        g = segment.Gear
        return thePlayer.roll(g)

    def move(self, thePlayer):
        pos = self.roll(thePlayer).Value
        advLeft = self.RoadHandler.advancePlayer(thePlayer, pos)
        return thePlayer.RoadPos, advLeft

    def init(self):
        self._createPlayers()
        self.Road = basicRoad()
        self.RoadHandler = RoadHandler(self.Road)
        for p in self._players:
            self.RoadHandler.addPlayer(p)


g = Game()
g.init()
p = []
for i in range(g.NbrOfPlayers):
    p.append(g.getPlayer(i))
