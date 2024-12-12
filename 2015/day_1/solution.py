from pathlib import Path


def load_input_puzzle():
    return (Path.cwd() / "input.txt.txt").read_text()


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


def get_enter_the_basement_position(puzzle: str) -> int:
    pos = 0

    up_char = "("
    down_char = ")"

    for i, ch in enumerate(puzzle, start=1):
        if ch == up_char:
            pos += 1

        elif ch == down_char:
            pos -= 1

        if pos == -1:
            return i


def main():
    puzzle = load_input_puzzle()

    print(get_floor_number(puzzle))

    print(get_enter_the_basement_position(puzzle))


if __name__ == '__main__':
    main()
