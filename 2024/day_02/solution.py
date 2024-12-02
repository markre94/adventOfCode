from helpers.input_loader import load_input


def load_input_codes():
    return [list(map(int, code.split())) for code in load_input().splitlines()]


def load_input_codes_test():
    x = """7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9"""
    return [list(map(int, code.split())) for code in x.splitlines()]


def check_levels(levels: list[int]):
    last_direction = ""
    direction = ""
    output = 1

    for i in range(len(levels) - 1):
        diff = levels[i] - levels[i + 1]
        print(f"{levels[i]} - {levels[i + 1]} = {diff}")

        if abs(diff) < 1 or abs(diff) > 3:
            output = 0
            break

        if diff > 0:
            direction = "-"
        elif diff < 0:
            direction = "+"

        if last_direction and last_direction != direction:
            output = 0
            break
        else:
            last_direction = direction

    if output == 1:
        print(f"{levels} are safe")
    else:
        print(f"{levels} are unsafe")

    return output


def verify_codes(input_data: list[list[int]]):
    return sum(check_levels(input_data[i]) for i in range(len(input_data)))


if __name__ == '__main__':
    data = load_input_codes()
    safe_codes = verify_codes(data)
    print(f"Number of save codes {safe_codes}")
