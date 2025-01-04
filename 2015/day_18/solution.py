from helpers.input_loader import load_input

grid = [list(line) for line in load_input().splitlines()]
r = len(grid)
c = len(grid[0])

ON = "#"
OFF = "."

neighbours = [
    (-1, 0), (0, -1), (0, 1), (1, 0), (1, -1), (-1, -1), (-1, 1), (1, 1)
]


def get_neighbours_states(x, y):
    states = []

    for dx, dy in neighbours:
        xx = x + dx
        yy = y + dy

        if (xx < 0 or xx >= r) or (yy < 0 or yy >= c):
            continue

        states.append(grid[xx][yy])
    return states


def count_on_lights():
    count = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == ON:
                count += 1

    return count


for _ in range(100):
    _grid = []
    for i in range(r):
        row = []
        for j in range(c):
            neighbours_states = get_neighbours_states(i, j)

            curr = grid[i][j]

            # Corners PART 2
            if i in (0, r - 1) and j in (0, c - 1):
                row.append(ON)
                continue

            if curr == ON:
                if neighbours_states.count(ON) not in (2, 3):
                    row.append(OFF)
                else:
                    row.append(ON)
            else:
                if neighbours_states.count(ON) == 3:
                    row.append(ON)
                else:
                    row.append(OFF)
        _grid.append(row)

    # Update GRID after each step
    grid = _grid[:]

print(count_on_lights())
