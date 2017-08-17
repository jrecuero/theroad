from road import RoadPos


class RoadHandler(object):

    def __init__(self, theRoad, theCars):
        self._road = theRoad
        self._cars = {}
        for p in theCars:
            self.addCar(p)

    def isFree(self, theRoadPos):
        # print('isFree at {0}'.format(theRoadPos))
        if theRoadPos.isStartPos():
            return True
        for _, p in self._cars.items():
            if p.RoadPos == theRoadPos:
                return False
        return True

    def carInRoadPos(self, theRoadPos):
        if theRoadPos.isStartPos():
            return True, None, None
        for n, p in self._cars.items():
            if p.RoadPos == theRoadPos:
                return False, n, p['car']
        return True, None, None

    def addCar(self, theCar):
        if theCar.Name in self._cars.keys():
            return False
        elif not self.isFree(theCar.RoadPos):
            return False
        else:
            self._cars[theCar.Name] = theCar
            return True

    def moveCarToRoadPos(self, theCar, theRoadPos):
        found, n, p = self.carInRoadPos(theRoadPos)
        if found:
            return True if (n == theCar.Name and p == theCar) else False
        else:
            theCar.RoadPos = theRoadPos
            return True

    def advanceCar(self, theCar, theAdvance):
        while True:
            nextPos = (theCar.RoadPos.Pos + 1) % self._road.Len
            _, segmentWidth = self._road.widthAt(nextPos)
            for newWidth, advPos in theCar.RoadPos.nextSideWidth(segmentWidth):
                nextPos = (theCar.RoadPos.Pos + 1) % self._road.Len
                newRoadPos = RoadPos(nextPos, newWidth)
                if self.isFree(newRoadPos):
                    theAdvance -= (advPos + 1)
                    if theAdvance >= 0:
                        theCar.RoadPos = newRoadPos

                    if theAdvance > 0:
                        break
                    else:
                        return theAdvance
            else:
                break
        return theAdvance
