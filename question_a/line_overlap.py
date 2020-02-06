"""
Question A
Your goal for this question is to write a program that accepts two lines
(x1, x2) and (x3, x4) on the x-axis and returns whether they overlap. As
an example, (1, 5) and (2, 6) overlaps but not (1, 5) and (6, 8).
"""

class Line:
    def __init__(self, start: int, end: int):
        """ Create a Line between 2 points """
        if end < start:
            end, start = start, end

        self.line = set(range(start, end))


class Overlap:
    def __init__(self, first_line: Line, second_line: Line):
        """ 2 Lines to be validated """
        self.first_line = first_line.line
        self.second_line = second_line.line

    def lines_overlaps(self):
        """ First Line Overlaps """
        first_overlap = self._overlaps(self.first_line, self.second_line)

        """ Second Line Overlaps """
        second_overlap = self._overlaps(self.second_line, self.first_line)

        return any([first_overlap, second_overlap])

    @staticmethod
    def _overlaps(line_a, line_b):
        return line_a.intersection(line_b)
