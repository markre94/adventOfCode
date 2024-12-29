from helpers.input_loader import load_input

data = load_input().splitlines()

res = {}


def load_instruction(line: str):
    lines = [int(elem.strip()) if elem.strip().isdigit() else elem.strip()
             for elem in line.split()]

    if len(lines) == 2:
        a, x = lines
        _x = res.get(x, x)

        # print(a, _x)
        return a, _x

    elif len(lines) == 3:
        x, a, y = lines

        _x = res.get(x, x)
        _y = res.get(y, y)

        # print(_x, a, _y)
        return _x, a, _y


def main():
    global res
    i = 0

    while True:
        if "a" in res:
            break
        element = data[i % len(data)]

        instruction, signal = [elem.strip()
                               for elem in element.split("->")]

        # PART 2
        if signal == "b":
            res[signal] = 46065

        if len(instruction.split()) == 1:
            # print(instruction, signal)
            if signal not in res:
                if instruction.isdigit():
                    res[signal] = int(instruction)
                else:
                    if instruction in res:
                        res[signal] = res[instruction]

        else:
            if "AND" in instruction:
                x, action, y = load_instruction(instruction)
                if isinstance(x, int) and isinstance(y, int):
                    res[signal] = x & y

            elif "OR" in instruction:
                x, action, y = load_instruction(instruction)

                if isinstance(x, int) and isinstance(y, int):
                    res[signal] = x | y

            elif "LSHIFT" in instruction:
                x, action, y = load_instruction(instruction)

                if isinstance(x, int) and isinstance(y, int):
                    res[signal] = x << y

            elif "RSHIFT" in instruction:
                x, action, y = load_instruction(instruction)

                if isinstance(x, int) and isinstance(y, int):
                    res[signal] = x >> y

            elif "NOT" in instruction:
                action, x = load_instruction(instruction)

                if isinstance(x, int):
                    res[signal] = ~x

        # print(len(res))
        i += 1

    print(res["a"])


if __name__ == '__main__':
    main()
