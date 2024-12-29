from helpers.input_loader import load_input

load = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

matrix = [list(elem) for elem in load_input().splitlines()]

m = len(matrix)
n = len(matrix[0])

word = "XMAS"

directions = [
    (0, 1),  # right
    (1, 1),  # right down
    (1, 0),  # down
    (1, -1),  # down left
    (0, -1),  # left
    (-1, -1),  # left up
    (-1, 0),  # up
    (-1, 1)  # right, up
]

counter = 0


def check_direction(row, col, dx, dy):
    for i, ch in enumerate(word):
        new_row = row + i * dx
        new_col = col + i * dy

        if not (0 <= new_row < m and 0 <= new_col < n) or matrix[new_row][new_col] != ch:  # boundary check
            return False
    return True


for r in range(m):
    for c in range(n):
        for dxx, dyy in directions:
            if check_direction(r, c, dxx, dyy):
                counter += 1


print(counter)
