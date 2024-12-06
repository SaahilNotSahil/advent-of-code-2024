import re


def mul(x, y):
    return x * y


muls = []

pattern = re.compile("mul\(\d{1,3},\d{1,3}\)")

with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        muls.extend(pattern.findall(line))

sum = 0

for m in muls:
    x, y = map(int, m[4:-1].split(","))

    sum += mul(x, y)

print(sum)
