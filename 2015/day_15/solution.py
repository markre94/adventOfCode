import re

from helpers.input_loader import load_input
from itertools import combinations_with_replacement
from functools import reduce
from operator import mul

mapped = {}

input_data = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""


for d in load_input().splitlines():
    name = re.match('\w+', d).group()
    mapped[name] = list(map(int, re.findall(r"-?\d+", d)))

print(mapped)


res = (d for d in combinations_with_replacement(range(0, 101), 4) if sum(d) == 100)

total_score = 0

# res = [(40, 60), (99, 1)]

for r in res:

    numbers = [0] * 5

    for p, v in zip(list(r), mapped.values()):
        data = [p * val for val in v]

        for i in range(len(numbers)):
            numbers[i] += data[i]

    if any(num < 0 for num in numbers[:-1]):
        continue
    else:
        together = reduce(mul, numbers[:-1])

        if numbers[-1] == 500:
            print(f"Changing total score: {r}, {numbers}")
            total_score = max(together, total_score)

print(total_score)
