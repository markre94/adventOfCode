import re
from typing import Callable

from helpers.input_loader import load_input

# register = {'children': '3', 'cats': '7', 'samoyeds': '2', 'pomeranians': '3', 'akitas': '0', 'vizslas': '0',
#             'goldfish': '5', 'trees': '3', 'cars': '2', 'perfumes': '1'}

register = {
    'children': 3,
    'cats': lambda val: val > 7,
    'samoyeds': 2,
    'pomeranians': lambda val: val < 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': lambda val: val < 5,
    'trees': lambda val: val > 3,
    'cars': 2,
    'perfumes': 1
}


def part_1():
    for i, data in enumerate(load_input().splitlines()):
        aunt_row = re.findall(r"\w+:\s\d+", data)
        row = {val.strip().split(":")[0].strip(): val.strip().split(":")[1].strip() for val in aunt_row}

        if all(item in register.items() for item in row.items()):
            print(i + 1)
            break


def part_2():
    for i, data in enumerate(load_input().splitlines()):
        aunt_row = re.findall(r"\w+:\s\d+", data)
        row = {val.strip().split(":")[0].strip(): int(val.strip().split(":")[1].strip()) for val in aunt_row}

        res = []
        for key, value in row.items():
            if isinstance(register[key], Callable):
                res.append(register[key](value))
            else:
                res.append(register[key] == value)

        if all(r for r in res):
            print(i + 1)
            break


part_2()
