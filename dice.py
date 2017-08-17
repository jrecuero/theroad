import random
from gear import Gear
import loggerator

logger = loggerator.getLoggerator('DICE')


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

    def __init__(self, theFaces, theGear=Gear.DIRECT):
        assert type(theFaces) in (list, tuple)
        self._faces = theFaces
        self._faceUp = None
        self._gear = theGear
        self._preRollCb = None
        self._rollCb = None
        self._postRollCb = None

    def roll(self):
        if self._preRollCb:
            self._preRollCb(self)

        if self._rollCb:
            self.FaceUp = self._rollCb(self)
        else:
            index = random.randint(0, self.NbrOfFaces - 1)
            self.FaceUp = self.Faces[index]

        if self._postRollCb:
            return self._postRollCb(self)
        else:
            return self.FaceUp

    @property
    def Faces(self):
        return self._faces

    @property
    def NbrOfFaces(self):
        return len(self._faces)

    @property
    def FaceUp(self):
        return self._faceUp

    @FaceUp.setter
    def FaceUp(self, theValue):
        self._faceUp = theValue

    @property
    def Gear(self):
        return self._gear

    @property
    def Value(self):
        return self.FaceUp.Value if self.FaceUp else None

    @property
    def Gas(self):
        return self.FaceUp.Gas if self.FaceUp else None

    @property
    def Tire(self):
        return self.FaceUp.Tire if self.FaceUp else None

    def setCbs(self, thePreRollCb, theRollCb, thePostRollCb):
        self._preRollCb = thePreRollCb if thePreRollCb else self._preRollCb
        self._rollCb = theRollCb if theRollCb else self._rollCb
        self._postRollCb = thePostRollCb if thePostRollCb else self._postRollCb

    def __repr__(self):
        _ = [str(x.Value) for x in self._faces]
        return '[{0}]'.format(', '.join(_))


class DiceSet(object):

    def __init__(self, theDices, theGear=Gear.DIRECT):
        assert type(theDices) in (list, tuple)
        assert all([dice.Gear == theGear for dice in theDices])
        self._dices = theDices
        self._facesUp = None
        self._gear = theGear

    def roll(self):
        self.FacesUp = []
        for dice in self._dices:
            self.FacesUp.append(dice.roll())
        logger.debug('dice roll [{0}]: {1}'.format(self.Gear, self.Value))
        return self.FacesUp

    @property
    def Dices(self):
        return self._dices

    @property
    def NbrOfDices(self):
        return len(self._dices)

    @property
    def FacesUp(self):
        return self._facesUp

    @FacesUp.setter
    def FacesUp(self, theValue):
        self._facesUp = theValue

    @property
    def Gear(self):
        return self._gear

    @property
    def Value(self):
        return [face.Value for face in self.FacesUp] if self.FacesUp else None

    @property
    def Gas(self):
        return [face.Gas for face in self.FacesUp] if self.FacesUp else None

    @property
    def Tire(self):
        return [face.Tire for face in self.FacesUp] if self.FacesUp else None

    @property
    def Result(self):
        if self.FacesUp is None:
            return None
        result = DiceResult()
        result.Faces = self.FacesUp
        result.Value = sum(self.Value)
        result.Gas = sum(self.Gas)
        result.Tire = sum(self.Tire)
        return result

    def __repr__(self):
        _ = [str(x) for x in self._dices]
        return '{0} * {1}'.format(self.Gear, ' * '.join(_))


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
        self._faces = None
        self._value = 0
        self._gas = 0
        self._tire = 0

    @property
    def Faces(self):
        return self._faces

    @Faces.setter
    def Faces(self, theValue):
        self._faces = theValue

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
