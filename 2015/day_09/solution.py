from helpers.input_loader import load_input
from itertools import permutations

graph = {}
cities = set()

for line in load_input().splitlines():
    data = line.split()

    cities.add(data[0])
    cities.add(data[2])

    graph[(data[0], data[2])] = int(data[-1])
    graph[(data[2], data[0])] = int(data[-1])

cities = (perm for perm in permutations(cities))
shortest_path = float("inf")
longest_path = 0

for data in cities:
    path = sum(graph.get((c, cc)) for c, cc in zip(data, data[1:]) if (c, cc) in graph)
    shortest_path = min(path, shortest_path)
    longest_path = max(path, longest_path)

print(shortest_path)
print(longest_path)