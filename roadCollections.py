from road import Segment, Road
from gear import Gear


def basicRoad(self):
    r = Road()
    r.addSegment(Segment(100, Gear.DIRECT))
    r.addSegment(Segment(50, Gear.TURN))
    r.addSegment(Segment(100, Gear.DIRECT))
    r.addSegment(Segment(50, Gear.TURN))
    return r
