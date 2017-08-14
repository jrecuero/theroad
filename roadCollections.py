from road import Segment, Road
from gear import Gear


def basicRoad():
    r = Road()
    r.addSegment(Segment(100, theGear=Gear.DIRECT))
    r.addSegment(Segment(50, theGear=Gear.TURN))
    r.addSegment(Segment(100, theGear=Gear.DIRECT))
    r.addSegment(Segment(50, theGear=Gear.TURN))
    return r
