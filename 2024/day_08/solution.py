from itertools import combinations
from math import gcd

from helpers.input_loader import load_input
from string import ascii_letters, digits

data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

accepted_antennas = ascii_letters + digits

lines = [[ch for ch in line] for line in load_input().splitlines()]
r = len(lines)
c = len(lines[0])

antennas: dict[str, list] = {}

for i in range(r):
    for j in range(c):
        if lines[i][j] in accepted_antennas:
            if lines[i][j] in antennas:
                antennas[lines[i][j]].append((i, j))
            else:
                antennas[lines[i][j]] = [(i, j)]

antinodes = set()

for coords in antennas.values():
    print()
    for (start_y, start_x), (end_y, end_x) in combinations(coords, 2):
        print((start_y, start_x), (end_y, end_x))

        dy = start_y - end_y
        dx = start_x - end_x
        gc = gcd(dy, dx)
        dy //= gc
        dx //= gc

        i = 0
        while True:
            aa = (start_x + dx * i, start_y + dy * i)
            if 0 <= aa[0] < r and 0 <= aa[1] < c:
                antinodes.add(aa)
                i += 1
            else:
                break
        i = 0
        while True:
            bb = (end_x - dx * i, end_y - dy * i)
            if 0 <= bb[0] < r and 0 <= bb[1] < c:
                antinodes.add(bb)
                i += 1
            else:
                break

print(len(antinodes))
