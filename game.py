import car
from roadCollections import basicRoad
from roadHandler import RoadHandler


class Game(object):

    def __init__(self, theNbrOfCars=3):
        self._road = None
        self._cars = []
        self._nbfOfCars = theNbrOfCars
        self._roadHandler = None

    def _createCars(self):
        for i in range(self._nbfOfCars):
            p = car.Car('car{0}'.format(i), theUser=True if i == 0 else False)
            p.init()
            self._cars.append(p)

    @property
    def Road(self):
        return self._road

    @Road.setter
    def Road(self, theRoad):
        self._road = theRoad

    @property
    def RoadHandler(self):
        return self._roadHandler

    @RoadHandler.setter
    def RoadHandler(self, theRoadHandler):
        self._roadHandler = theRoadHandler

    @property
    def NbrOfCars(self):
        return self._nbfOfCars

    def getCarByIndex(self, theIndex):
        return self._cars[theIndex]

    def getCarByName(self, theName):
        for i, p in enumerate(self._cars):
            if p.Name == theName:
                return i, p
        return None, None

    def roll(self, theCar):
        pos = theCar.Pos
        _, segment = self.Road.segmentAt(pos)
        g = segment.Gear
        return theCar.roll(g)

    def move(self, theCar):
        adv = self.roll(theCar).Value
        advLeft = self.RoadHandler.advanceCar(theCar, adv)
        return adv, theCar.RoadPos, advLeft

    def init(self):
        self._createCars()
        self.Road = basicRoad()
        self.RoadHandler = RoadHandler(self.Road, self._cars)
