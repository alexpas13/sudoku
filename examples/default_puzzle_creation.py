import logging

from puzzle import Puzzle

logging.basicConfig(level=logging.DEBUG)

table = Puzzle.create()
table.show()
