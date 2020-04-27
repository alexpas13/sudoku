import logging

from helpers.table import Table
from puzzle import Puzzle

logging.basicConfig(level=logging.DEBUG)


matrix = [
    ["3", None, "4", "5", None, "9", None, None, None],
    ["6", "7", "8", "4", "1", None, "9", None, None],
    [None, None, "5", None, None, None, None, None, None],
    [None, None, None, None, None, "6", None, None, "5"],
    ["9", "6", None, "1", "3", None, "7", None, "4"],
    ["5", None, None, None, "7", None, "2", None, "1"],
    [None, None, "7", "3", "9", "2", "6", "1", None],
    ["1", None, "9", None, "8", "4", None, "3", "7"],
    ["8", None, "6", "7", "5", None, "4", "2", None],
]

table = Table(size=9, matrix=matrix)

solution = Puzzle.solve(table)
solution.show()
