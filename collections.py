import Gear
from dice import Face, Dice, DiceSet, Collection


def basicCollection(self):
    _collection = Collection()
    _dice = Dice(6, [Face(1), Face(2), Face(3), Face(4), Face(5), Face(6)])
    _diceSet = DiceSet(3, [_dice, _dice, _dice])
    _collection.addToCollection(Gear.DIRECT, _diceSet)
    _dice = Dice(3, [Face(1), Face(2), Face(3)], Gear.TURN)
    _diceSet = DiceSet(2, [_dice, _dice], Gear.TURN)
    _collection.addToCollection(Gear.TURN, _diceSet)
    return _collection
