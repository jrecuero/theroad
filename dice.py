import random


class Face(object):

    def __init__(self, theValue):
        self._value = theValue

    @property
    def Value(self):
        return self._value


class Dice(object):

    def __init__(self, theNbrOfFaces, theFaces):
        assert theNbrOfFaces == len(theFaces)
        assert type(theFaces) in (list, tuple)
        self.nbrFaces = theNbrOfFaces
        self.faces = theFaces
        self.selectedFace = None

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

    def __init__(self, theNbrOfDices, theDices):
        assert theNbrOfDices == len(theDices)
        assert type(theDices) in (list, tuple)
        self.nbrFaces = theNbrOfDices
        self.dices = theDices
        self.selectedFaces = None

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
