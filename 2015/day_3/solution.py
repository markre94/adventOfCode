from helpers.input_loader import load_input


def get_data():
    data_in = load_input()
    return data_in


def get_number_of_houses(in_data):
    pos_set = set()
    pos_x, pos_y = 0, 0

    north = "^"
    east = ">"
    west = "<"
    south = "v"

    for char in in_data:

        if char == north:
            pos_y += 1
        elif char == east:
            pos_x += 1
        elif char == west:
            pos_x -= 1
        elif char == south:
            pos_y -= 1

        current_position = (pos_x, pos_y)
        pos_set.add(current_position)

    return len(pos_set)


def get_number_of_houses_with_robot(in_data):
    pos_set = set()
    pos_x, pos_y = 0, 0
    pos_x_robot, pos_y_robot = 0, 0

    north = "^"
    east = ">"
    west = "<"
    south = "v"

    for i in range(0, len(in_data), 2):
        direction_santa, direction_robot = in_data[i:i + 2]

        if direction_santa == north:
            pos_y += 1
        elif direction_santa == east:
            pos_x += 1
        elif direction_santa == west:
            pos_x -= 1
        elif direction_santa == south:
            pos_y -= 1

        current_position = (pos_x, pos_y)
        pos_set.add(current_position)

        if direction_robot == north:
            pos_y_robot += 1
        elif direction_robot == east:
            pos_x_robot += 1
        elif direction_robot == west:
            pos_x_robot -= 1
        elif direction_robot == south:
            pos_y_robot -= 1

        robot_position = (pos_x_robot, pos_y_robot)
        pos_set.add(robot_position)

    return len(pos_set)


if __name__ == '__main__':
    data = get_data()

    print(get_number_of_houses(data))
    print("####")
    print(get_number_of_houses_with_robot(data))
