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

corners = [
    (-1, 1),  # right, up
    (1, 1),  # right down
    (-1, -1),  # left up
    (1, -1),  # down left
]


def part2(x, y, mat):
    if not (1 <= x < n - 1 and 1 <= y < m - 1):
        return False

    w1 = mat[x - 1][y - 1] + mat[x][y] + mat[x + 1][y + 1]
    w2 = mat[x + 1][y - 1] + mat[x][y] + mat[x - 1][y + 1]

    if w1 in ['MAS', 'SAM'] and w2 in ['MAS', 'SAM']:
        return True
    return False


counter = 0

for r in range(m):
    for c in range(n):
        if part2(r, c, matrix):
            counter += 1

print(counter)
