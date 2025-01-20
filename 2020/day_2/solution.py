from collections import Counter

from helpers.input_loader import load_input

data = [data.split() for data in load_input().splitlines()]


def part_1():
    res = 0
    for line in data:
        range_ = list(map(int, line[0].split("-")))
        letter = line[1].rstrip(":")
        c = Counter(line[-1])

        if c[letter] in range(range_[0], range_[1] + 1):
            res += 1

    print(res)


def xor(a, b):
    return (a and not b) or (not a and b)


def part_2():
    res = 0
    for line in data:
        num1, num2 = list(map(int, line[0].split("-")))
        letter = line[1].rstrip(":")
        letters = line[-1]

        indexes = [i for i, l in enumerate(letters, 1) if l == letter]
        a = num1 in indexes
        b = num2 in indexes

        if xor(a, b):
            res += 1

    return res


print(part_2())
