class Segment(object):

    def __init__(self, theLength):
        self._length = theLength

    @property
    def Len(self):
        return self._length


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
