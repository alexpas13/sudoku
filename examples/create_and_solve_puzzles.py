from puzzle import Difficulty, Puzzle

params = (
    (9, Difficulty.hardest),
    (4, Difficulty.hard),
    (9, Difficulty.middle),
    (16, Difficulty.easy),
    (4, Difficulty.easiest),
)

for size, difficulty in params:
    print("-" * 41)
    print(f"Puzzle {size}X{size} with {difficulty}")
    table = Puzzle.create(size=size, difficulty=difficulty)
    table.show()
    solution = Puzzle.solve(table)
    solution.show()
