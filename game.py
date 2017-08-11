import road
import dice
import player


class Game(object):

    def __init__(self):
        self._road = None
        self._dices = None
        self._player = player.Player('player')
        self._createDices()
        self._createRoad()

    @property
    def Road(self):
        return self._road

    @Road.setter
    def Road(self, theRoad):
        self._road = theRoad

    @property
    def Dices(self):
        return self._dices

    @property
    def Player(self):
        return self._player

    def _createRoad(self):
        self.Road = road.Road()
        self.Road.addSegment(road.Segment(100))

    def _createDices(self):
        _dice = dice.Dice(3, [dice.Face(1), dice.Face(2), dice.Face(3)])
        self._dices = dice.DiceSet(2, [_dice, _dice])

    def roll(self):
        self.Dices.roll()
        return self.Dices.Value

    def move(self):
        pos = sum(self.roll())
        self.Player.Pos += pos
        return self.Player.Pos
