import road
import player


class Game(object):

    def __init__(self):
        self._road = None
        self._player = player.Player('player')

    @property
    def Road(self):
        return self._road

    @Road.setter
    def Road(self, theRoad):
        self._road = theRoad

    @property
    def Player(self):
        return self._player

    def _createRoad(self):
        self.Road = road.Road()
        self.Road.addSegment(road.Segment(100))

    def roll(self):
        pos = self.Player.Pos
        index, _ = self.Road.segmentAt(pos)
        segment = self.Road[index]
        g = segment.Gear
        return self.Player.roll(g)

    def move(self):
        pos = self.roll().Value
        self.Player.Pos += pos
        return self.Player.Pos

    def init(self):
        self.Player.init()
        self._createRoad()
