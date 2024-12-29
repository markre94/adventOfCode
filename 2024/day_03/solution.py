from helpers.input_loader import load_input
import re


def get_multiplications_result():
    data = load_input()

    r = re.findall(r"mul\(\d{,3},\d{,3}\)|do\(\)|don\'t\(\)", data)

    results = []
    enabled = True

    for res in r:
        if res == "do()":
            enabled = True
            continue
        elif res == "don't()":
            enabled = False
            continue

        print(res)

        if enabled:
            results.append(tuple(map(int, res[4:-1].split(','))))

    return sum(x * y for x, y in results)


if __name__ == '__main__':
    ress = get_multiplications_result()
    print(ress)
