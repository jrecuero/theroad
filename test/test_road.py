import pytest
from road import Road, Segment


@pytest.fixture
def baseRoad(request):
    _ = Road()
    print('\n')
    try:
        lengths = request.param
    except AttributeError:
        lengths = []
    for length in lengths:
        _.addSegment(Segment(length))
        print('adding segment with length {}'.format(length))
    print('road created')
    return _


@pytest.fixture(params=[[10, 20, 30, 50]])
def roadTest(request, baseRoad):
    baseRoad.create(*request.param)
    print('test road created')
    return baseRoad


def test_Road(baseRoad):
    assert baseRoad._index == 0
    assert baseRoad._segments == []
    assert baseRoad._endAt == 0


@pytest.mark.parametrize('theLengths', [[10], [10, 20], [10, 20, 30]])
def test_addSegment(baseRoad, theLengths):
    for length in theLengths:
        baseRoad.addSegment(Segment(length))
    index = len(theLengths)
    assert len(baseRoad._segments) == index
    assert baseRoad._endAt == sum(theLengths)
    # start, end = 0, 0
    # for i, v in enumerate(theLengths):
    #     end += v
    #     assert baseRoad._road[i] == {'start': start, 'end': end}
    #     start += v


@pytest.mark.parametrize('theLengths', [[10], [10, 20], [10, 20, 30]])
def test_create(baseRoad, theLengths):
    baseRoad.create(*theLengths)
    index = len(theLengths)
    assert len(baseRoad._segments) == index
    assert baseRoad._endAt == sum(theLengths)
    # start, end = 0, 0
    # for i, v in enumerate(theLengths):
    #     end += v
    #     assert baseRoad._road[i] == {'start': start, 'end': end}
    #     start += v


@pytest.mark.parametrize('theLengths', [[10], [10, 20], [10, 20, 30]])
def test_full_road(baseRoad, theLengths):
    baseRoad.create(*theLengths)
    for i, length in enumerate(theLengths):
        assert baseRoad[i].Len == length
    for s, l in zip(baseRoad, theLengths):
        assert s.Len == l


@pytest.mark.parametrize('thePos, theExpectation', [(5, 0), (15, 1), (67, 3), (2, 0), (81, 3)])
def test_segmentAt(roadTest, thePos, theExpectation):
    i, _ = roadTest.segmentAt(thePos)
    assert i == theExpectation


@pytest.mark.parametrize('theLimits', [(10, 20, 30, 50)])
def test_segmentAt_full(roadTest, theLimits):
    trav = 0
    for ind, nextEnd in enumerate(theLimits):
        for pos in range(trav, trav + nextEnd):
            i, seg = roadTest.segmentAt(pos)
            assert i == ind
            assert seg.EndAt == trav + nextEnd
        trav += nextEnd
