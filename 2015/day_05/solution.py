from collections import defaultdict

from helpers.input_loader import load_input

data_ = [
    "ugknbfddgicrmopn",
    "aaa",
    "jchzalrnumimnmhp",
    "haegwjzuvuyypxyu",
    "haegwjzuvuyypxyu"
]


def count_nice_strings(input_data: list[str]):
    vowels = ["a", "e", "i", "o", "u"]
    forbidden_substrings = ["ab", "cd", "pq", "xy"]
    counted_strings = 0

    for elem in input_data:
        if any(substring in elem for substring in forbidden_substrings):
            continue

        if not any(x == y for x, y in zip(elem, elem[1:])):
            continue

        if sum(1 for ch in elem if ch in vowels) < 3:
            continue

        counted_strings += 1

    return counted_strings


def count_nice_strings_part_2(input_data: list[str]):
    counted_strings = 0

    for line in input_data:
        first, second = False, False

        pairs = defaultdict(int)
        indexes = defaultdict(list)

        for i in range(0, len(line) - 1):
            elem = "".join(line[i: i + 2])
            indexes[elem].extend([i, i + 1])

            if len(set(indexes[elem])) == len(indexes[elem]):
                pairs[elem] += 1

        print(indexes)
        if any(val > 1 for val in pairs.values()):
            first = True
        else:
            continue

        for i in range(0, len(line) - 2):
            elem = line[i: i + 3]
            # print(one, two, three)
            if elem[0] == elem[2]:
                # print(elem)
                second = True

        if first and second:
            print(f"Match: {line}")
            counted_strings += 1

    return counted_strings


if __name__ == '__main__':
    data = load_input().splitlines()
    result = count_nice_strings_part_2(data)
    print(f"Number of nice strings: {result}")
