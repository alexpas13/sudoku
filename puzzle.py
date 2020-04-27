from enum import Enum

from helpers.solver import Solver
from helpers.table import Table


class Difficulty(Enum):
    hardest = 1
    hard = 0.65
    middle = 0.55
    easy = 0.45
    easiest = 0.35


class Puzzle:
    @staticmethod
    def create(size=9, difficulty=Difficulty.middle):
        table = Table(size=size)
        table.shuffle()
        solver = Solver(table)

        while True:
            cell = solver.get_min_variant_cell(table.filled_cells)
            value = table.clear(cell)

            if not solver.has_one_solution():
                table.exclude_cells.append(cell)
                table.set(value, cell)

            if table.empty_cell_percent() > difficulty.value:
                return table

            if len(table.filled_cells) == len(table.exclude_cells):
                return table

    @staticmethod
    def solve(table: Table):
        solutions = Solver(table).get_solutions()
        return solutions[0]
