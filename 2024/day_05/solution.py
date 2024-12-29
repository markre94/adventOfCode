from helpers.input_loader import load_input


def load():
    data = load_input().split()
    rules = []
    printing = []
    for d in data:
        if "|" in d:
            rules.append(d)
        else:
            printing.append(d)


if __name__ == '__main__':
    load()
