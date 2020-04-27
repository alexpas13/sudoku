import logging
from random import shuffle
from typing import Set, Tuple, List

from helpers.table import Table

logger = logging.getLogger(__name__)


class Solver:
    def __init__(self, table: Table):
        self.table = table

    def available_values(self, cell: Tuple[int, int]) -> Set[str]:
        x, y = cell
        return (
            set(self.table.values) -
            self.row_values(x) -
            self.column_values(y) -
            self.block_values(x, y)
        )

    def available_value_count(self, cell: Tuple[int, int]) -> int:
        return len(self.available_values(cell))

    def get_min_variant_cell(self, cells):
        shuffle(cells)
        cell = min(cells, key=self.available_value_count)
        logger.debug(f"Cell with minimal variants of values found: {cell}")
        return cell

    def row_values(self, x: int) -> Set[str]:
        values = set(self.table.matrix[x])
        if None in values:
            values.remove(None)
        return values

    def column_values(self, y: int) -> Set[str]:
        transposed_table = list(zip(*self.table.matrix))
        values = set(transposed_table[y])
        if None in values:
            values.remove(None)
        return values

    def block_values(self, x: int, y: int) -> Set[str]:
        block_row = x // self.table.block_count
        block_column = y // self.table.block_count

        x_begin = block_row * self.table.block_size
        x_end = x_begin + self.table.block_size

        y_begin = block_column * self.table.block_size
        y_end = y_begin + self.table.block_size

        values = set()
        for row in self.table.matrix[x_begin:x_end]:
            values |= set(row[y_begin:y_end])

        return values

    def get_solutions(self) -> List[Table]:
        solutions = []
        cell = self.get_min_variant_cell(self.table.empty_cells)
        candidates = self.available_values(cell)
        logger.info(f"Candidates for {cell} found: {','.join(candidates)}")
        for value in candidates:
            table = self.table.copy()
            table.set(value, cell)

            if table.empty_cells:
                result = Solver(table).get_solutions()
                solutions.extend(result)
            else:
                solutions.append(table)

                logger.info(f"Solution found")
                logger.info(table)

        return solutions

    def has_one_solution(self):
        counter = 0
        cell = self.get_min_variant_cell(self.table.empty_cells)
        candidates = self.available_values(cell)
        for value in candidates:
            table = self.table.copy()
            table.set(value, cell)

            if table.empty_cells:
                result = Solver(table).has_one_solution()
                if result:
                    counter += result
                else:
                    return
            else:
                counter += 1

            if counter > 1:
                logger.info(f"Puzzle has more than two solutions")
                return

        return counter
