from road import RoadPos


class Car(object):

    def __init__(self, theName, theCollection, **kwargs):
        assert theName
        assert theCollection
        self._name = theName
        self._collection = theCollection
        self._roadPos = kwargs.get('theRoadPos', RoadPos())
        self._user = kwargs.get('theUser', False)
        self._ai = kwargs.get('theAi', False if self.IsUser else True)
        assert self._user != self._ai
        self._runProc = None
        self._preRollCb = None
        self._rollCb = None
        self._postRollCb = None

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
        if self._preRollCb:
            diceSet = self._preRollCb(self, theGear)
        else:
            diceSet = self.Collection.getDice(theGear)

        if self._rollCb:
            result = self._rollCb(self, theGear)
        else:
            # print('dice-set: {0}'.format(diceSet))
            diceSet.roll()
            result = diceSet.Result

        if self._postRollCb:
            return self._postRollCb(self, theGear, result)
        else:
            return result

    def init(self, theRunProc):
        self.Run = theRunProc()
        next(self.Run)
        self.Run.send(self)

    def setCbs(self, thePreRollCb, theRollCb, thePostRollCb):
        self._preRollCb = thePreRollCb if thePreRollCb else self._preRollCb
        self._rollCb = theRollCb if theRollCb else self._rollCb
        self._postRollCb = thePostRollCb if thePostRollCb else self._postRollCb

    def __repr__(self):
        side = 'user' if self.IsUser else 'ai'
        return '[{0}] {1} road: {2}'.format(side, self.Name, self.RoadPos)
