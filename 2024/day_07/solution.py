from helpers.input_loader import load_input
import itertools

ops = ['+', '*', "||"]

data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def concat(a, b):
    return int(f"{a}{b}")


ans = 0

for line in load_input().splitlines():
    split_line = line.split(":")
    x = int(split_line[0])
    y = [int(num) for num in split_line[1].strip().split()]

    perms = [p for p in itertools.product(ops, repeat=len(y) - 1)]

    for p in perms:
        result = y[0]
        for n, s in itertools.zip_longest(y[1:], p, fillvalue=""):
            if s == "+":
                result += n
            elif s == "*":
                result *= n
            else:
                result = concat(result, n)

        # print(result)
        if result == x:
            ans += x
            break

print(ans)
