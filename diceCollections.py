from gear import Gear
from dice import Face, Dice, DiceSet, Collection

FACE_1 = Face(1)
FACE_2 = Face(2)
FACE_3 = Face(3)
FACE_4 = Face(4)
FACE_5 = Face(5)
FACE_6 = Face(6)

DICE_1 = [FACE_1]
DICE_2 = [FACE_1, FACE_2]
DICE_3 = [FACE_1, FACE_2, FACE_3]
DICE_4 = [FACE_1, FACE_2, FACE_3, FACE_4]
DICE_5 = [FACE_1, FACE_2, FACE_3, FACE_4, FACE_5]
DICE_6 = [FACE_1, FACE_2, FACE_3, FACE_4, FACE_5, FACE_6]


def basicCollection():
    _collection = Collection()
    _dice = Dice(DICE_6)
    _diceSet = DiceSet([_dice] * 3, Gear.DIRECT)
    _collection.addToCollection(_diceSet.Gear, _diceSet)

    _dice = Dice(DICE_3, Gear.TURN)
    _diceSet = DiceSet([_dice] * 2, Gear.TURN)
    _collection.addToCollection(_diceSet.Gear, _diceSet)
    return _collection
