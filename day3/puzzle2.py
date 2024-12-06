import re


def mul(x, y):
    return x * y


muls = []

pattern1 = re.compile("don't\(\)")
pattern2 = re.compile("mul\(\d{1,3},\d{1,3}\)")
pattern3 = re.compile("do\(\)")

donts = []

with open("input.txt", "r") as f:
    lines = "".join(f.readlines())

donts.extend(pattern1.split(lines))

muls.extend(pattern2.findall(donts[0]))

donts = donts[1:]

for dont in donts:
    dos = pattern3.split(dont)[1:]

    for do in dos:
        muls.extend(pattern2.findall(do))

sum = 0

for m in muls:
    x, y = map(int, m[4:-1].split(","))

    sum += mul(x, y)

print(sum)
