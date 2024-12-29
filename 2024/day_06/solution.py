from itertools import cycle
from helpers.input_loader import load_input

data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

matrix = [[ch for ch in line] for line in load_input().splitlines()]
r = len(matrix)
c = len(matrix[0])

pos = (0, 0)
positions = set()

for i in range(r):
    for j in range(c):
        if matrix[i][j] == "^":
            pos = (i, j)
            positions.add(pos)

x, y = pos

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
end = False

for direction in cycle(directions):

    if end:
        break

    while True:
        dx, dy = direction
        xx = x + dx
        yy = y + dy

        if not (0 <= xx < r and 0 <= yy < c):
            end = True
            break

        if matrix[xx][yy] == "#":
            break
        else:
            positions.add((xx, yy))
            x = xx
            y = yy

print(f"Positions: {len(positions)}")
