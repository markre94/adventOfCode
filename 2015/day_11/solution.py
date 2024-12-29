from collections import defaultdict

data = "hxbxwxba"


def is_password_valid(s: str):
    res = [ord(ch) for ch in data]

    if any(val in res for val in [ord("i"), ord("o"), ord("l")]):
        return False

    pairs = set([s[i:i + 2] for i in range(0, len(s), 2)])
    if len(pairs) < 2:
        return False

    threes = [s[i: i + 3] for i in range(len(s) - 2)]
    print(threes)

    return True


while not is_password_valid(data):
    data_ = [ord(ch) for ch in data]

    data = "".join([chr(num) for num in data_])

print(data)
