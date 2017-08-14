# from road import RoadPos
# import player


class RoadHandler(object):

    def __init__(self, theRoad):
        self._road = theRoad
        self._players = {}

    def isFree(self, theRoadPos):
        if theRoadPos.isStartPos():
            return True
        for _, p in self._players.items():
            if p['road_pos'] == theRoadPos:
                return False
        return True

    def playerInRoadPos(self, theRoadPos):
        if theRoadPos.isStartPos():
            return True, None, None
        for n, p in self._players.items():
            if p['road_pos'] == theRoadPos:
                return False, n, p['player']
        return True, None, None

    def addPlayer(self, thePlayer):
        if thePlayer.Name in self._players.keys():
            return False
        elif not self.isFree(thePlayer.RoadPos):
            return False
        else:
            self._players[thePlayer.Name] = {'player': thePlayer, 'road_pos': thePlayer.RoadPos}
            return True

    def movePlayerToRoadPos(self, thePlayer, theRoadPos):
        found, n, p = self.playerInRoadPos(theRoadPos)
        if found:
            return True if (n == thePlayer.Name and p == thePlayer) else False
        else:
            thePlayer.RoadPos = theRoadPos
            return True
