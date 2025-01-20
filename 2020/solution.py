from helpers.input_loader import load_input


def part_1():
    data = list(map(int, load_input().split()))

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == 2020:
                return data[i] * data[j]


# print(part_1())


def part_2():
    hash_map = {}
    data = list(map(int, load_input().split()))
    target = 2020

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x, y = data[i], data[j]
            hash_map[x + y] = [x, y]

    for i in range(len(data)):
        if val := hash_map.get(target - data[i]):
            return data[i] * val[0] * val[1]


print(part_2())
