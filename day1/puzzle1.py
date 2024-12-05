list1 = []
list2 = []

with open("input1.txt", "r") as f:
    while 1:
        try:
            nums = list(map(int, f.readline().strip().split("  ")))
            list1.append(nums[0])
            list2.append(nums[1])
        except Exception:
            break

sum = 0

for i, j in zip(sorted(list1), sorted(list2)):
    sum += abs(i - j)

print(sum)
