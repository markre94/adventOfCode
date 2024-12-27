from helpers.input_loader import load_input
import ast

res_literals = 0
res_chars = 0
x = r"aaa\"aaa"


def transform_string(s: str):
    return ast.literal_eval(s)


def encode(s):
    result = ''
    for c in s:
        if c == '"':
            result += "\\\""
        elif c == '\\':
            result += "\\\\"
        else:
            result += c
    return '"' + result + '"'


res_enc = 0

for line in load_input().splitlines():
    res_literals += len(line)
    res_chars += len(transform_string(line))
    res_enc += len(encode(line))
#     x = 0
print(res_literals - res_chars)

print(res_enc - res_literals)
