from pathlib import Path


def load_input_puzzle():
    return (Path.cwd() / "input.txt").read_text()


def get_floor_number(puzzle: str):
    floor_hash_map = {}

    for ch in puzzle:
        if ch in floor_hash_map:
            floor_hash_map[ch] += 1
        else:
            floor_hash_map[ch] = 1

    result_floor = floor_hash_map["("] - floor_hash_map[")"]

    print(result_floor)

    return result_floor


def main():
    puzzle = load_input_puzzle()

    print(get_floor_number(puzzle))


if __name__ == '__main__':
    main()
