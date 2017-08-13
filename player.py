from diceCollections import basicCollection


class Player(object):

    def __init__(self, theName, thePos=0):
        self._name = theName
        self._pos = thePos
        self._collection = None

    @property
    def Name(self):
        return self._name

    @property
    def Pos(self):
        return self._pos

    @Pos.setter
    def Pos(self, thePos):
        self._pos = thePos

    @property
    def Collection(self):
        return self._collection

    def roll(self, theGear):
        diceSet = self.Collection.getDice(theGear)
        diceSet.roll()
        return diceSet.Result

    def init(self):
        self._collection = basicCollection()
