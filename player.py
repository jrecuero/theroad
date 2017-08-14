from diceCollections import basicCollection
from road import RoadPos


class Player(object):

    def __init__(self, theName, **kwargs):
        self._name = theName
        self._roadPos = kwargs.get('theRoadPos', RoadPos())
        self._user = kwargs.get('theUser', False)
        self._ai = kwargs.get('theAi', True)
        assert self._user != self._ai
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

    @property
    def IsUser(self):
        return self._user

    @property
    def IsAi(self):
        return self._ai

    def roll(self, theGear):
        diceSet = self.Collection.getDice(theGear)
        diceSet.roll()
        return diceSet.Result

    def init(self):
        self._collection = basicCollection()
