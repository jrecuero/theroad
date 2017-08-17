import car
from roadCollections import basicRoad
from roadHandler import RoadHandler


class Game(object):

    def __init__(self, theNbrOfCars=3):
        self._road = None
        self._cars = []
        self._nbfOfCars = theNbrOfCars
        self._roadHandler = None
        self._time = 0

    def _createCars(self):
        for i in range(self._nbfOfCars):
            c = car.Car('car{0}'.format(i), theUser=True if i == 0 else False)
            self.addCar(c)

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

    @property
    def Cars(self):
        return self._cars

    @property
    def Time(self):
        return self._time

    @Time.setter
    def Time(self, theValue):
        self._time = theValue

    def addCar(self, theCar):
        if self.getCarByName(theCar.Name) == (None, None):
            self._cars.append(theCar)
            theCar.init(self.carProcess)
            return True
        return False

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

    def sorted(self):
        return sorted(self._cars, key=lambda x: x.RoadPos.Pos, reverse=True)

    def init(self):
        self._createCars()
        self.Road = basicRoad()
        self.RoadHandler = RoadHandler(self.Road, self._cars)

    def tick(self):
        for c in self.sorted():
            adv, roadPos, advLeft = next(c.Run)
            self.Time += 1

    def carProcess(self):
        _car = yield
        yield _car.RoadPos
        while True:
            # adv = self.roll(_car).Value
            # advLeft = self.RoadHandler.advanceCar(_car, adv)
            # yield adv, _car.RoadPos, advLeft
            yield self.move(_car)
