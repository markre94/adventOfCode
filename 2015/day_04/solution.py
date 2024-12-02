import hashlib


def find_input():
    number = 0
    puzzle = f"bgvyzdsv{number}"
    target = "0" * 6

    while True:

        val = hashlib.md5(puzzle.encode()).hexdigest()

        if val.startswith(target):
            return number

        number += 1
        puzzle = f"bgvyzdsv{number}"


if __name__ == '__main__':
    val = find_input()
    print(val)
