import random

from helpers.input_loader import load_input
import re
from random import shuffle


def part_1():
    _data = load_input().splitlines()
    text = _data[-1]
    rules = [d.split(" => ") for d in _data[:-2]]
    # print(rules)
    # print(text)

    values = set()

    for r in rules:
        ch, replace_value = r
        indexes = [m.start() for m in re.finditer(ch, text)]

        for index in indexes:
            end_index = index + len(ch)
            s = text[:index] + replace_value + text[end_index:]
            values.add(s)

    print(len(values))


def part_2():
    _data = load_input().splitlines()
    text = _data[-1]
    rules = [d.split(" => ")[::-1] for d in _data[:-2]]

    target = text

    count = 0
    while target != 'e':
        tmp = target
        for a, b in rules:
            if a not in target:
                continue

            target = target.replace(a, b, 1)
            count += 1

        if tmp == target:
            target = text
            count = 0
            shuffle(rules)

    return count


print(part_2())
