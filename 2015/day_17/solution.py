import itertools

from helpers.input_loader import load_input

containers = list(map(int, load_input().splitlines()))
print(containers)


def part_1():
    count = 0
    for i in range(1, len(containers) + 1):
        for subset in itertools.combinations(containers, i):
            print(subset)
            if sum(subset) == 150:
                count += 1

    print(count)


def find_min_number_of_containers():
    count = 0
    for i in range(1, len(containers) + 1):
        for subset in itertools.combinations(containers, i):
            if len(subset) == 4 and sum(subset) == 150:
                count += 1
    return count


part_1()
print(find_min_number_of_containers())
