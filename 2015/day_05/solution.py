from helpers.input_loader import load_input

data = [
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

    for elem in input_data:
        if any([x == z and y not in (x, z) for x, y, z in zip(elem, elem[1:], elem[2:])]):
            continue

        if not any(x == y for x, y in zip(elem, elem[1:])):
            continue

        if sum(1 for ch in elem if ch in vowels) < 3:
            continue

        counted_strings += 1

    return counted_strings


if __name__ == '__main__':
    data = load_input().splitlines()
    result = count_nice_strings(data)
    print(f"Number of nice strings: {result}")
