from road import RoadPos
# import player


class RoadHandler(object):

    def __init__(self, theRoad, thePlayers):
        self._road = theRoad
        self._players = {}
        for p in thePlayers:
            self.addPlayer(p)

    def isFree(self, theRoadPos):
        # print('isFree at {0}'.format(theRoadPos))
        if theRoadPos.isStartPos():
            return True
        for _, p in self._players.items():
            if p.RoadPos == theRoadPos:
                return False
        return True

    def playerInRoadPos(self, theRoadPos):
        if theRoadPos.isStartPos():
            return True, None, None
        for n, p in self._players.items():
            if p.RoadPos == theRoadPos:
                return False, n, p['player']
        return True, None, None

    def addPlayer(self, thePlayer):
        if thePlayer.Name in self._players.keys():
            return False
        elif not self.isFree(thePlayer.RoadPos):
            return False
        else:
            self._players[thePlayer.Name] = thePlayer
            return True

    def movePlayerToRoadPos(self, thePlayer, theRoadPos):
        found, n, p = self.playerInRoadPos(theRoadPos)
        if found:
            return True if (n == thePlayer.Name and p == thePlayer) else False
        else:
            thePlayer.RoadPos = theRoadPos
            return True

    def advancePlayer(self, thePlayer, theAdvance):
        while True:
            nextPos = (thePlayer.RoadPos.Pos + 1) % self._road.Len
            _, segmentWidth = self._road.widthAt(nextPos)
            for newWidth, advPos in thePlayer.RoadPos.nextSideWidth(segmentWidth):
                nextPos = (thePlayer.RoadPos.Pos + 1) % self._road.Len
                newRoadPos = RoadPos(nextPos, newWidth)
                if self.isFree(newRoadPos):
                    theAdvance -= (advPos + 1)
                    if theAdvance >= 0:
                        thePlayer.RoadPos = newRoadPos

                    if theAdvance > 0:
                        break
                    else:
                        return theAdvance
            else:
                break
        return theAdvance
