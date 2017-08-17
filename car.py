from diceCollections import basicCollection
from road import RoadPos


class Car(object):

    def __init__(self, theName, **kwargs):
        self._name = theName
        self._roadPos = kwargs.get('theRoadPos', RoadPos())
        self._user = kwargs.get('theUser', False)
        self._ai = kwargs.get('theAi', False if self.IsUser else True)
        assert self._user != self._ai
        self._collection = None
        self._runProc = None

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

    @property
    def Run(self):
        return self._runProc

    @Run.setter
    def Run(self, theValue):
        self._runProc = theValue

    def roll(self, theGear):
        diceSet = self.Collection.getDice(theGear)
        # print('dice-set: {0}'.format(diceSet))
        diceSet.roll()
        return diceSet.Result

    def init(self, theRunProc):
        self._collection = basicCollection()
        self.Run = theRunProc()
        next(self.Run)
        self.Run.send(self)

    def __repr__(self):
        side = 'user' if self.IsUser else 'ai'
        return '[{0}] {1} road: {2}'.format(side, self.Name, self.RoadPos)
