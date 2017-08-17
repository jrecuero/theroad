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
        self._preTickCb = None
        self._tickCb = None
        self._postTickCb = None

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

    def advanceTime(self, theAdvTime=1):
        self.Time += theAdvTime

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

    def setCbs(self, thePreTickCb, theTickCb, thePostTickCb):
        self._preTickCb = thePreTickCb if thePreTickCb else self._preTickCb
        self._tickCb = theTickCb if theTickCb else self._tickCb
        self._postTickCb = thePostTickCb if thePostTickCb else self._postTickCb

    def tick(self, theNbrOfTicks=1):
        for t in range(theNbrOfTicks):
            if self._preTickCb:
                self._preTickCb(self)

            if self._tickCb:
                self._tickCb(self)
            else:
                for c in self.sorted():
                    adv, roadPos, advLeft = next(c.Run)
                self.AdvanceTime()

            if self._postTickCb:
                self._postTickCb(self)

    def init(self):
        self._createCars()
        self.Road = basicRoad()
        self.RoadHandler = RoadHandler(self.Road, self._cars)

    def carProcess(self):
        _car = yield
        yield _car.RoadPos
        while True:
            yield self.move(_car)
