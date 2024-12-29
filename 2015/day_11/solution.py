from itertools import pairwise

# data = "hxbxwxba"
data = "hxbxxyzz"


def is_password_valid(s: str):
    res = [ord(ch) for ch in data]

    if any(val in res for val in [ord("i"), ord("o"), ord("l")]):
        return False

    pairs = set()

    for i in range(len(s) - 1):
        pair = s[i: i + 2]
        if len(set(pair)) == 1:
            pairs.add(pair)

    if len(pairs) < 2:
        return False

    threes = [res[i: i + 3] for i in range(len(s) - 2)]
    found = False
    for three in threes:
        if set([y - x for (x, y) in pairwise(three)]) == {1}:
            found = True
            break

    if not found:
        return False

    return True


def increment_string(c: str):
    c = list(c)
    for i in range(len(c) - 1, 0, -1):
        if c[i] == "z":
            c[i] = chr((ord(c[i]) - ord('a') + 1) % 26 + ord('a'))
        else:
            increment = 1
            if c[i] in ("h", "n", "k"):
                increment = 2
            c[i] = chr((ord(c[i]) - ord('a') + increment) % 26 + ord('a'))
            break
    return "".join(c)


# Part 1
# while not is_password_valid(data):
#     data = increment_string(data)
#     print(data)

# Part 2
data = increment_string(data)
while not is_password_valid(data):
    data = increment_string(data)
    # print(data)

print(data)
