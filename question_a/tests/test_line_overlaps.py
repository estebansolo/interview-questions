import pytest
from question_a.line_overlap import Line, Overlap

lines_overlaps = [
    ((-2, 1), (0, 3), True),
    ((6, -2), (-2, 6), True),
    ((-2, 0), (-4, 0), True),
    ((-5, -4), (-4, -3), False),
    ((-5, -3), (-2, -3), False),
]
    
@pytest.mark.parametrize("first_line,second_line,expected", lines_overlaps)
def test_overlaps(first_line, second_line, expected):
    """ Validate if two lines overlaps """

    overlaps = Overlap(Line(*first_line), Line(*second_line))
    assert overlaps.lines_overlaps() == expected



line_points = [
    ((-2, 1), (-2, 1)),
    ((-5, -11), (-11, -5)),
    ((1, 6), (1, 6)),
    ((0, -2), (-2, 0)),
    ((6, 1), (1, 6)),
]
    
@pytest.mark.parametrize("points,expected", line_points)
def test_line_points(points, expected):
    """ When the end is less than the start point, it swaps the numbers """
    
    line = Line(*points)
    start, end = expected
    assert line.line == set(range(start, end))