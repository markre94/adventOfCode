import re

from helpers.input_loader import load_input, load_input_as_json

data_ = load_input()
digits = [int(elem) for elem in re.findall(r"-?\d+", data_)]
print(sum(digits))


def sum_numbers(obj):
    if type(obj) is dict:
        if "red" in obj.values():
            return 0

        return sum([sum_numbers(values) for values in obj.values()])

    elif type(obj) is list:
        return sum([sum_numbers(values) for values in obj])

    elif type(obj) is int:
        return obj

    return 0


num = sum_numbers(load_input_as_json())
print(num)
