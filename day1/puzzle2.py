list1 = []
list2 = []

with open("input2.txt", "r") as f:
    while 1:
        try:
            nums = list(map(int, f.readline().strip().split("  ")))
            list1.append(nums[0])
            list2.append(nums[1])
        except Exception:
            break

sum = 0

for i in list1:
    sum += i * list2.count(i)

print(sum)
