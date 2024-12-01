from pathlib import Path


def _load_puzzle(puzzle: str) -> tuple[list[int], list[int]]:
    first, second = [], []

    for line in puzzle.splitlines():
        x, y = line.split()
        first.append(int(x))
        second.append(int(y))

    return first, second


def load_puzzle():
    puzzle = """3   4
    4   3
    2   5
    1   3
    3   9
    3   3"""

    return _load_puzzle(puzzle)


def load_puzzle_from_file() -> tuple[list, list]:
    puzzle_content = (Path.cwd() / "input.txt").read_text()
    return _load_puzzle(puzzle_content)


def get_total_distance(list_1: list[int], list_2: list[int]):
    return [abs(elem_1 - elem_2) for elem_1, elem_2 in zip(sorted(list_1), sorted(list_2))]


def calculate_similarity_score(list_1: list[int], list_2: list[int]) -> list[int]:
    counted_list_1_elements = {}
    similarities = []

    for elem in list_1:
        if elem not in counted_list_1_elements:
            counted_list_1_elements[elem] = elem * list_2.count(elem)

        similarities.append(counted_list_1_elements[elem])

    return similarities


def main():
    lists = load_puzzle_from_file()

    total_distance = get_total_distance(*lists)
    print(f"Total distance is: {sum(total_distance)}")

    print(f"Similarities in lists: {sum(calculate_similarity_score(*lists))}")


if __name__ == '__main__':
    main()
