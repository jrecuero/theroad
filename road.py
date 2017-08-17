from gear import Gear


class Segment(object):

    def __init__(self, theLength, **kwargs):
        self._length = theLength
        self._width = kwargs.get("theWidth", 2)
        self._height = kwargs.get("theHeight", 0)
        self._gear = kwargs.get("theGear", Gear.DIRECT)
        self._startAt = None
        self._endAt = None

    def placeInRoad(self, theStartAt, theEndAt):
        assert theEndAt  - theStartAt == self.Len
        self._startAt = theStartAt
        self._endAt = theEndAt

    @property
    def Len(self):
        return self._length

    @property
    def Width(self):
        return self._width

    @property
    def Height(self):
        return self._height

    @property
    def Gear(self):
        return self._gear

    @property
    def StartAt(self):
        return self._startAt

    @property
    def EndAt(self):
        return self._endAt


class Road(object):

    def __init__(self):
        self._index = 0
        self._segments = []
        self._endAt = 0

    @property
    def Len(self):
        return self._endAt

    def addSegment(self, theSegment):
        assert type(theSegment) == Segment
        assert theSegment.Len > 0
        _ = self._endAt + theSegment.Len
        theSegment.placeInRoad(self._endAt, _)
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
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self._segments):
            self._index = 0
            raise StopIteration
        _ = self._segments[self._index]
        self._index += 1
        return _

    def __len__(self):
        return len(self._segments)

    def segmentAt(self, thePos):
        for index, seg in enumerate(self):
            if thePos < seg.EndAt:
                return index, seg
        return None, None

    def widthAt(self, thePos):
        index, seg = self.segmentAt(thePos)
        return index, seg.Width if seg else None

    def gearAt(self, thePos):
        index, seg = self.segmentAt(thePos)
        return index, seg.Gear if seg else None


class RoadPos(object):

    def __init__(self, thePos=0, theWidth=0, theRacePos=0):
        self._pos = thePos
        self._width = theWidth
        self._racePos = theRacePos

    @property
    def Pos(self):
        return self._pos

    @property
    def Width(self):
        return self._width

    @property
    def RacePos(self):
        return self._racePos

    def __repr__(self):
        return "RoadPos: {0}-{1}/{2}".format(self.Pos, self.RacePos, self.Width)

    def __eq__(self, theOther):
        if isinstance(theOther, self.__class__):
            # print('{0} __eq__ {1}'.format(self, theOther))
            return (self.Pos == theOther.Pos) and (self.Width == theOther.Width)
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

    def nextSideWidth(self, theWidth):
        width, inc = (self.Width, 0) if self.Width < theWidth else (theWidth - 1, 1)
        yield width, inc
        plus, minus = True, True
        for inc in range(1, theWidth):
            if plus:
                newWidth = width + inc
                if newWidth < theWidth:
                    yield newWidth, inc
                else:
                    plus = False
            if minus:
                newWidth = width - inc
                if newWidth >= 0:
                    yield newWidth, inc
                else:
                    minus = False

    def isStartPos(self):
        return self.Pos == 0 and self.Width == 0
