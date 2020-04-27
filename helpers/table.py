import logging
import math
from random import randint
from typing import List, Union, Tuple

logger = logging.getLogger(__name__)


class Table:
    VALUES = [
        "1", "2", "3", "4",
        "5", "6", "7", "8",
        "9", "0", "A", "B",
        "C", "D", "E", "F",
    ]

    SIZES = [4, 9, 16]

    def __init__(
            self,
            size: int,
            matrix: List[List[Union[str, None]]] = None,
            values: List[str] = None,
            filled_cells: List[Tuple[int, int]] = None,
            empty_cells: List[Tuple[int, int]] = None,
            exclude_cells: List[Tuple[int, int]] = None,
    ):
        self.size = size
        self.block_count = int(math.sqrt(size))
        self.block_size = int(math.sqrt(size))
        self.values = values or self.VALUES[:size]
        self.matrix = matrix or self._get_initial_matrix()
        self.filled_cells = filled_cells or self._get_filled_cells()
        self.empty_cells = empty_cells or self._get_empty_cells()
        self.exclude_cells = exclude_cells or []

    def copy(self):
        return Table(
            size=self.size,
            matrix=[[e for e in row] for row in self.matrix],
            filled_cells=[e for e in self.filled_cells],
            empty_cells=[e for e in self.empty_cells],
            exclude_cells=[e for e in self.exclude_cells],
        )

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in self.SIZES:
            raise Exception(
                f"Size value {value}"
                f"should be equals one from {self.SIZES}"
            )
        self._size = value

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        if len(values) < self.size:
            raise Exception(
                f"Values count {len(values)} "
                f"should be equals or more than {self.size}"
            )
        self._values = values

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        x = len(matrix)
        y = len(list(zip(matrix)))
        if x != self.size or x != self.size:
            raise Exception(
                f"Matrix size {x}x{y} us invalid, "
                f"should be {self.size}x{self.size}"
            )
        self._matrix = matrix

    def _get_filled_cells(self) -> List[Union[Tuple[int, int], None]]:
        cells = []
        for x, row in enumerate(self.matrix):
            for y, value in enumerate(row):
                if value:
                    cells.append((x, y))
        return cells

    def _get_empty_cells(self):
        cells = []
        for x, row in enumerate(self.matrix):
            for y, value in enumerate(row):
                if not value:
                    cells.append((x, y))
        return cells

    def _get_initial_matrix(self):
        table = []
        for i in range(self.size):
            n = (i // self.block_count + i * self.block_size) % self.size
            table.append(self.values[n:self.size] + self.values[:n])
        logger.info(f"Start table {self.size}X{self.size} is got")
        logger.debug(table)
        return table

    def transpose(self):
        self.matrix = list(map(list, zip(*self.matrix)))

        logger.info(f"Table is transposed")
        logger.debug(self)

    def change_rows(self):
        block_index = randint(0, self.block_count - 1)
        row_1_index = (
                randint(0, self.block_size - 1) + block_index * self.block_size
        )

        row_2_index = row_1_index
        while row_1_index == row_2_index:
            row_2_index = (
                    randint(0, self.block_size - 1)
                    + block_index * self.block_size
            )

        row_1 = self.matrix[row_1_index]
        row_2 = self.matrix[row_2_index]
        self.matrix[row_1_index], self.matrix[row_2_index] = row_2, row_1

        logger.info(f"Rows {row_1_index} and {row_2_index} are changed")
        logger.info(f"Row {row_1_index}: {row_1}")
        logger.info(f"Row {row_2_index}: {row_2}")
        logger.debug(self)

    def change_columns(self):
        self.transpose()
        self.change_rows()
        self.transpose()

    def change_row_blocks(self):
        block_1_index = randint(0, self.block_count - 1)

        block_2_index = block_1_index
        while block_1_index == block_2_index:
            block_2_index = randint(0, self.block_count - 1)

        for row_index in range(self.block_size):
            row_1_index = row_index + block_1_index * self.block_size
            row_2_index = row_index + block_2_index * self.block_size
            row_1 = self.matrix[row_1_index]
            row_2 = self.matrix[row_2_index]
            self.matrix[row_1_index], self.matrix[row_2_index] = row_2, row_1

        logger.info(
            f"Block rows {block_1_index} and {block_2_index} are changed"
        )
        first_row = block_1_index * self.block_size
        logger.info(
            f"Block row {block_1_index}: "
            f"{self.matrix[first_row:first_row + self.block_size]}"
        )
        first_row = block_2_index * self.block_size
        logger.info(
            f"Block row {block_2_index}: "
            f"{self.matrix[first_row:first_row + self.block_size]}"
        )
        logger.debug(self)

    def change_column_blocks(self):
        self.transpose()
        self.change_row_blocks()
        self.transpose()

    def random_action(self):
        actions = [
            "change_rows",
            "change_columns",
            "change_row_blocks",
            "change_column_blocks",
        ]
        name = actions[randint(0, 3)]
        getattr(self, name)()

    def shuffle(self, depth=30):
        for _ in range(depth):
            self.random_action()
        if randint(0, 1):
            self.transpose()

    def __str__(self):
        hr = "-" * (self.size * 2 + self.block_count * 2 + 1) + "\n"
        s = "\n"
        s += hr
        for x, row in enumerate(self.matrix):
            s += "| "
            for y, num in enumerate(row):
                s += f"{num} " if num else "  "

                if not (y + 1) % self.block_size:
                    s += "| "

            s += "\n"

            if not (x + 1) % self.block_count:
                s += hr

        return s

    def set(self, value: Union[str, None], cell: Tuple[int, int]):
        x, y = cell
        self.matrix[x][y] = value
        self.filled_cells.append(cell)
        self.empty_cells.remove(cell)

        logger.info(f"Value {value} for {cell} is set")
        logger.debug(self)

    def clear(self, cell: Tuple[int, int]) -> str:
        x, y = cell
        value = self.matrix[x][y]
        self.matrix[x][y] = None
        self.empty_cells.append(cell)
        self.filled_cells.remove(cell)
        logger.info(f"Value {value} for {cell} is removed")
        logger.debug(self)
        return value

    def empty_cell_percent(self):
        return len(self.empty_cells) / (self.size * self.size)

    def show(self):
        print(self)
