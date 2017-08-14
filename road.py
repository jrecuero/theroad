from gear import Gear


class Segment(object):

    def __init__(self, theLength, theWidth=2, theGear=Gear.DIRECT):
        self._length = theLength
        self._width = theWidth
        self._gear = theGear

    @property
    def Len(self):
        return self._length

    @property
    def Width(self):
        return self._width

    @property
    def Gear(self):
        return self._gear


class Road(object):

    def __init__(self):
        self._index = 0
        self._segments = []
        self._road = {}
        self._endAt = 0

    def addSegment(self, theSegment):
        assert type(theSegment) == Segment
        assert theSegment.Len > 0
        _ = self._endAt + theSegment.Len
        segmentIndex = len(self._segments)
        self._road[segmentIndex] = {'start': self._endAt, 'end': _}
        self._endAt = _
        self._segments.append(theSegment)

    def create(self, *args):
        for length in args:
            self.addSegment(Segment(length))

    def __getitem__(self, theKey):
        assert theKey < len(self._segments)
        return self._segments[theKey]

    def __setitem__(self, theKey, theValue):
        assert theKey < len(self._segments)
        assert type(theValue) == Segment
        self._segments[theKey] = theValue

    def __delitem(self, theKey):
        assert theKey < len(self._segments)
        del self._segments[theKey]

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._segments):
            self._index = 0
            raise StopIteration
        _ = self._segments[self._index]
        self._index += 1
        return _

    def segmentAt(self, thePos):
        for index, seg in self._road.items():
            if thePos < seg['end']:
                return index, seg


class RoadPos(object):

    def __init__(self, thePos=0, theWidth=0):
        self._pos = thePos
        self._width = theWidth

    @property
    def Pos(self):
        return self._pos

    @property
    def Width(self):
        return self._width

    def __eq__(self, theOther):
        if isinstance(theOther, self.__class__):
            return self.Pos == theOther.Pos and self.Width == theOther.Width
        return NotImplemented

    def __ne__(self, theOther):
        if isinstance(theOther, self.__class__):
            return not self.__eq__(theOther)
        return NotImplemented

    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object).
        """
        return hash(tuple(sorted(self.__dict__.items())))

    def __add__(self, thePos):
        if type(thePos) == int:
            pos = self.Pos + thePos
            width = self.Width
            return RoadPos(pos, width)
        return NotImplemented

    def __radd__(self, thePos):
        if type(thePos) == int:
            if thePos == 0:
                return self
            else:
                return self.__add__(thePos)
        return NotImplemented

    def isStartPos(self):
        return self.Pos == 0 and self.Width == 0
