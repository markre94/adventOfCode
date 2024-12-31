from dataclasses import dataclass, field

from helpers.input_loader import load_input


@dataclass
class Reindeer:
    name: str
    speed: int
    move_time: int
    rest_time: int
    points: int = field(default_factory=int)
    total_distance: int = field(default_factory=int)

    def calculate_distance(self, total_time):
        speed = self.speed
        fly_time = self.move_time
        rest_time = self.rest_time

        cycle_time = fly_time + rest_time

        full_cycles = total_time // cycle_time

        remaining_time = total_time % cycle_time

        distance_full_cycles = full_cycles * (speed * fly_time)

        effective_remaining_time = min(remaining_time, fly_time)
        distance_remaining = speed * effective_remaining_time

        total_distance = distance_full_cycles + distance_remaining

        self.total_distance = total_distance


data = []
for d in load_input().splitlines():
    data_ = d.split()
    name = data_[0]
    speed = int(data_[3])
    move_time = int(data_[6])
    rest_time = int(data_[-2])
    data.append(Reindeer(name, speed, move_time, rest_time))

max_dist = 0
points = 0
time = 2503

for i in range(1, time + 1):
    for d in data:
        d.calculate_distance(i)
        max_dist = max(max_dist, d.total_distance)

    for d in data:
        if d.total_distance == max_dist:
            d.points += 1

print(max_dist)
print(max([d.points for d in data]))
