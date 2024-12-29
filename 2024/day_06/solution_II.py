from copy import deepcopy
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


def find_starting_pos(m):
    for i in range(r):
        for j in range(c):
            if m[i][j] == "^":
                pos = (i, j)
                return pos


def find_positions():
    pos = (0, 0)
    positions = set()

    x, y = find_starting_pos(matrix)
    positions.add((x, y))

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

    return positions


count_obstacle = 0

for posx, posy in list(find_positions()):
    new_matrix = deepcopy(matrix)
    if new_matrix[posx][posy] not in ["^", "#"]:
        new_matrix[posx][posy] = "#"

        positions = set()
        x, y = find_starting_pos(new_matrix)

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        end = False
        is_loop = False

        for direction in cycle(directions):

            if end:
                break

            if is_loop:
                count_obstacle += 1
                break

            while True:
                dx, dy = direction
                xx = x + dx
                yy = y + dy

                if not (0 <= xx < r and 0 <= yy < c):
                    end = True
                    break

                if new_matrix[xx][yy] == "#":
                    break
                else:
                    if (xx, yy, dx, dy) in positions:
                        is_loop = True
                        break

                    positions.add((xx, yy, dx, dy))
                    x = xx
                    y = yy

print(count_obstacle)

