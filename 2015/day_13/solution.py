from itertools import permutations

from helpers.input_loader import load_input

persons = set()
hash_map = {}


def load_data():
    global persons, hash_map

    for line in load_input().splitlines():
        data = line.split()
        p1 = data[0]
        sign = -1 if data[2] == "lose" else 1
        value = int(data[3])
        p2 = data[-1].rstrip(".")

        persons.add(p1)
        persons.add(p2)

        hash_map[(p1, p2)] = sign * value


def part_1():
    load_data()
    pp = (list(p) for p in permutations(persons))

    most_optimal = 0

    for val in pp:
        pairs = [[(x, y), (y, x)] for x, y in zip(val, val[1:] + [val[0]])]
        _optimal = 0
        for p in pairs:
            _optimal += sum([hash_map[elem] for elem in p])

        most_optimal = max(most_optimal, _optimal)

    print(most_optimal)


def part_2():
    load_data()
    global persons
    persons.add("Marcin")

    pp = (list(p) for p in permutations(persons))

    most_optimal = 0

    for val in pp:
        pairs = [[(x, y), (y, x)] for x, y in zip(val, val[1:] + [val[0]])]
        _optimal = 0
        for p in pairs:
            _optimal += sum([hash_map[elem] if "Marcin" not in elem else 0 for elem in p])

        most_optimal = max(most_optimal, _optimal)

    print(most_optimal)


if __name__ == '__main__':
    part_1()
