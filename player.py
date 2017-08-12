from gear import Gear
from dice import Face, Dice, DiceSet, Collection


class Player(object):

    def __init__(self, theName, thePos=0):
        self._name = theName
        self._pos = thePos
        self._collection = Collection()

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

    def _createCollection(self):
        _dice = Dice(6, [Face(1), Face(2), Face(3), Face(4), Face(5), Face(6)])
        _diceSet = DiceSet(3, [_dice, _dice, _dice])
        self.Collection.addToCollection(Gear.DIRECT, _diceSet)
        _dice = Dice(3, [Face(1), Face(2), Face(3)], Gear.TURN)
        _diceSet = DiceSet(2, [_dice, _dice], Gear.TURN)
        self.Collection.addToCollection(Gear.TURN, _diceSet)

    def roll(self, theGear):
        dice = self.Collection.getDice(theGear)
        dice.roll()
        return dice.Value

    def init(self):
        self._createCollection()
