# Sudoku

This project was created to generate and solve of sudoku puzzles.

## How to create a sudoku puzzle

For generation of a new puzzle you need to use the method `create` from the static class `Puzzle`.

#### Parameters of `Puzzle.create`:
- `size` is side size, it should be equal 4, 9 or 16 (9 by default)
- `difficulty` is initial percentage of completion, to set standard level use `Difficulty` enum with values easiest, easy, middle, hard or hardest (middle by default)

#### Example:
```python
from puzzle import Difficulty, Puzzle

table = Puzzle.create(size=9, difficulty=Difficulty.hard)
table.show()
```    
#### Example of output:       
``` 
-------------------------
|       | 9 2 1 |     5 | 
|       |     4 |   6 8 | 
| 4 3 5 |       |       | 
-------------------------
| 6   7 | 8     | 3     | 
| 9     |       | 6 5 7 | 
| 3   4 | 5 7   | 9     | 
-------------------------
| 8 7 9 | 1     |       | 
|   1 3 | 4   5 |     9 | 
|   4   |       | 2     | 
-------------------------
```

## How to solve a sudoku puzzle:
To solve a puzzle You need to create object `Table` and use it in the method `solve` from the static class `Puzzle`. 
#### Parameters of `Table`:
- `size` is side size, it should be equal the matrix side (required)
- `matrix` is 2d list filled by `str` or `None`, matrix sides should be equal 4, 9 or 16
- `values` need to use if the matrix has non-standard value (by default 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E, F)
#### Parameters of `Puzzle.solve`:
- `table` is `Table` object
```python
from helpers.table import Table
from puzzle import Puzzle

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

solution: Table = Puzzle.solve(table)
solution.show()
```
#### Example of output:
```
-------------------------
| 3 1 4 | 5 2 9 | 8 7 6 | 
| 6 7 8 | 4 1 3 | 9 5 2 | 
| 2 9 5 | 8 6 7 | 1 4 3 | 
-------------------------
| 7 8 1 | 2 4 6 | 3 9 5 | 
| 9 6 2 | 1 3 5 | 7 8 4 | 
| 5 4 3 | 9 7 8 | 2 6 1 | 
-------------------------
| 4 5 7 | 3 9 2 | 6 1 8 | 
| 1 2 9 | 6 8 4 | 5 3 7 | 
| 8 3 6 | 7 5 1 | 4 2 9 | 
-------------------------    
```
