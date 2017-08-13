import random
from gear import Gear


class Face(object):

    def __init__(self, theValue):
        self._value = theValue

    @property
    def Value(self):
        return self._value


class Dice(object):

    def __init__(self, theNbrOfFaces, theFaces, theGear=Gear.DIRECT):
        assert theNbrOfFaces == len(theFaces)
        assert type(theFaces) in (list, tuple)
        self.nbrFaces = theNbrOfFaces
        self.faces = theFaces
        self.selectedFace = None
        self.gear = theGear

    def roll(self):
        index = random.randint(0, self.nbrFaces - 1)
        self.selectedFace = self.faces[index]
        return self.selectedFace

    @property
    def Value(self):
        if self.selectedFace is None:
            return None
        return self.selectedFace.Value


class DiceSet(object):

    def __init__(self, theNbrOfDices, theDices, theGear=Gear.DIRECT):
        assert theNbrOfDices == len(theDices)
        assert type(theDices) in (list, tuple)
        assert all([dice.gear == theGear for dice in theDices])
        self.nbrFaces = theNbrOfDices
        self.dices = theDices
        self.selectedFaces = None
        self.gear = theGear

    def roll(self):
        self.selectedFaces = []
        for dice in self.dices:
            self.selectedFaces.append(dice.roll())
        return self.selectedFaces

    @property
    def Value(self):
        if self.selectedFaces is None:
            return self.selectedFaces
        return [face.Value for face in self.selectedFaces]

    @property
    def Result(self):
        if self.selectedFaces is None:
            return self.selectedFaces
        result = DiceResult()
        result.Value = sum(self.Value)
        return result


class Collection(object):

    def __init__(self):
        self._collection = Gear.getDict()

    @property
    def Collection(self):
        return self._collection

    def addToCollection(self, theGear, theDiceSet):
        self.Collection[theGear] = theDiceSet

    def getDice(self, theGear):
        return self.Collection[theGear]


class DiceResult(object):

    def __init__(self):
        self._value = 0

    @property
    def Value(self):
        return self._value

    @Value.setter
    def Value(self, theValue):
        self._value = theValue
