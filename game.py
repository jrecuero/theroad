import player
from roadCollections import basicRoad
from roadHandler import RoadHandler


class Game(object):

    def __init__(self, theNbrOfPlayers=3):
        self._road = None
        self._players = []
        self._nbfOfPlayers = theNbrOfPlayers
        self._roadHandler = None

    def _createPlayers(self):
        for i in range(self._nbfOfPlayers):
            p = player.Player('player{0}'.format(i), theUser=True if i == 0 else False)
            p.init()
            self._players.append(p)

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

    def getPlayerByIndex(self, theIndex):
        return self._players[theIndex]

    def getPlayerByName(self, theName):
        for i, p in enumerate(self._players):
            if p.Name == theName:
                return i, p
        return None, None

    def roll(self, thePlayer):
        pos = thePlayer.Pos
        _, segment = self.Road.segmentAt(pos)
        g = segment.Gear
        return thePlayer.roll(g)

    def move(self, thePlayer):
        adv = self.roll(thePlayer).Value
        advLeft = self.RoadHandler.advancePlayer(thePlayer, adv)
        return adv, thePlayer.RoadPos, advLeft

    def init(self):
        self._createPlayers()
        self.Road = basicRoad()
        self.RoadHandler = RoadHandler(self.Road, self._players)
