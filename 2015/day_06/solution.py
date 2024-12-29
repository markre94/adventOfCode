import re

from helpers.input_loader import load_input

grid = [[0 for i in range(1000)] for j in range(1000)]
r = len(grid)
c = len(grid[0])

turn_on = "turn on"
turn_off = "turn off"
toggle = "toggle"


def take_action(p11, p22, action: str):
    global grid

    for i in range(p11[0], p22[0] + 1):
        for j in range(p11[1], p22[1] + 1):

            if action == turn_on:
                grid[i][j] = 1
            elif action == turn_off:
                grid[i][j] = 0
            else:
                grid[i][j] = grid[i][j] ^ 1


def take_action_part_2(p11, p22, action: str):
    global grid

    for i in range(p11[0], p22[0] + 1):
        for j in range(p11[1], p22[1] + 1):

            if action == turn_on:
                # print(f"Increasing {grid[i][j]} by 1")

                grid[i][j] += 1
            elif action == turn_off:
                if grid[i][j]:
                    # print(f"Decreasing {grid[i][j]} by 1")
                    grid[i][j] -= 1
            else:
                # print(f"Increasing {grid[i][j]} by 2")
                grid[i][j] += 2


def main():
    global grid
    data = load_input().splitlines()

    for line in data:
        pattern = fr"{turn_on}|{turn_off}|{toggle}"
        action = re.match(pattern, line).group()

        # Get points
        p1, p2 = [tuple(map(int, corner.split(","))) for corner in re.findall(r"\d+,\d+", line)]
        # print(line)
        # print(p1, p2)
        print(action)

        take_action_part_2(p1, p2, action)


def count_turned_on_lights():
    res = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                res += 1
    return res


def count_brightness():
    return sum(sum(l) for l in grid)


if __name__ == '__main__':
    main()
    # print(grid)
    print(count_brightness())
