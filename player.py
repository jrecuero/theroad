from diceCollections import basicCollection
from road import RoadPos


class Player(object):

    def __init__(self, theName, theRoadPos=None):
        self._name = theName
        self._roadPos = theRoadPos if theRoadPos else RoadPos()
        self._collection = None

    @property
    def Name(self):
        return self._name

    @property
    def RoadPos(self):
        return self._roadPos

    @RoadPos.setter
    def RoadPos(self, theRoadPos):
        self._roadPos = theRoadPos

    @property
    def Pos(self):
        return self.RoadPos.Pos

    @property
    def Collection(self):
        return self._collection

    def roll(self, theGear):
        diceSet = self.Collection.getDice(theGear)
        diceSet.roll()
        return diceSet.Result

    def init(self):
        self._collection = basicCollection()
