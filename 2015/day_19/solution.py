from helpers.input_loader import load_input
import re

_data = load_input().splitlines()
text = _data[-1]
rules = [d.split(" => ") for d in _data[:-2]]
# print(rules)
# print(text)

values = set()

for r in rules:
    ch, replace_value = r
    indexes = [m.start() for m in re.finditer(ch, text)]

    for index in indexes:
        end_index = index + len(ch)
        s = text[:index] + replace_value + text[end_index:]
        values.add(s)

print(len(values))
