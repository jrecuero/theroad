import random
from gear import Gear


class Face(object):

    def __init__(self, theValue, theGas=0, theTire=0):
        self._value = theValue
        self._gas = theGas
        self._tire = theTire

    @property
    def Value(self):
        return self._value

    @property
    def Gas(self):
        return self._gas

    @property
    def Tire(self):
        return self._tire


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
        return self.selectedFace.Value if self.selectedFace else None

    @property
    def Gas(self):
        return self.selectedFace.Gas if self.selectedFace else None

    @property
    def Tire(self):
        return self.selectedFace.Tire if self.selectedFace else None


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
        return [face.Value for face in self.selectedFaces] if self.selectedFaces else None

    @property
    def Gas(self):
        return [face.Gas for face in self.selectedFaces] if self.selectedFaces else None

    @property
    def Tire(self):
        return [face.Tire for face in self.selectedFaces] if self.selectedFaces else None

    @property
    def Result(self):
        if self.selectedFaces is None:
            return None
        result = DiceResult()
        result.Value = sum(self.Value)
        result.Gas = sum(self.Gas)
        result.Tire = sum(self.Tire)
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
        self._gas = 0
        self._tire = 0

    @property
    def Value(self):
        return self._value

    @Value.setter
    def Value(self, theValue):
        self._value = theValue

    @property
    def Gas(self):
        return self._gas

    @Gas.setter
    def Gas(self, theValue):
        self._gas = theValue

    @property
    def Tire(self):
        return self._tire

    @Tire.setter
    def Tire(self, theValue):
        self._tire = theValue
