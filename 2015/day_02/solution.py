from helpers.input_loader import load_input


def get_data():
    data = load_input()
    return [
        [int(number) for number in elem.split("x")]
        for elem in data.splitlines()
    ]


def calculate_area(l, w, h):
    sides = set()

    side_lw = l * w
    side_wh = w * h
    side_hl = l * h

    sides.add(side_lw)
    sides.add(side_wh)
    sides.add(side_hl)

    area = 2 * side_lw + 2 * side_wh + 2 * side_hl

    return area + min(sides)


def get_shortest_distance(l, w, h):
    side_lw = 2 * l + 2 * w
    side_wh = 2 * w + 2 * h
    side_hl = 2 * l + 2 * h

    shortest_perm = min([side_lw, side_wh, side_hl])
    bow = l * w * h

    return shortest_perm + bow


def calculate_feet_of_ribbon(input_data):
    return sum(get_shortest_distance(l, w, h) for l, w, h in input_data)


def calculate_paper_surface(input_data):
    return sum(calculate_area(l, w, h) for l, w, h in input_data)


if __name__ == '__main__':
    _data = get_data()
    print(calculate_paper_surface(_data))
    print(calculate_feet_of_ribbon(_data))
