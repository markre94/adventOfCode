import time
from itertools import groupby
from pathlib import Path
from helpers.input_loader import load_input

start_time = time.time()
input_lines = "2333133121414131402".splitlines()
disk_map = [int(value) for value in input_lines[0]]

EMPTY_SLOT = -1
res = []
block_id = 0
current_block_id = -1


for index, count in enumerate(disk_map):
    if index % 2 == 0:
        current_block_id += 1
    res.append({
        "id": current_block_id if index % 2 == 0 else EMPTY_SLOT,
        "count": count
    })


def calculate_checksum(blocks: list):
    return sum([i * int(num) for i, num in enumerate(blocks) if num != "."])


start = 0
end = len(res) - 1
i = start

# groups = [list(g) for k, g in groupby(res)]
# print(groups)
print(res)

while start < end:
    right_most_numbers = [list(g) for k, g in groupby(res) if k != -1][-1]
    leftmost_space = []

    while res[start] == EMPTY_SLOT and start < end:
        leftmost_space.append(start)
        start += 1

    print(leftmost_space)
    start += 1


print("--- %s seconds ---" % (time.time() - start_time))
print("result", calculate_checksum(res))
