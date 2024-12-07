with open("input.txt", "r") as f:
    lines = f.readlines()

grid = [list(line.strip()) for line in lines]

height = len(grid)
width = len(grid[0])

for i in range(height):
    grid[i] = ["Z"] + grid[i] + ["Z"]

grid = [["Z"] * len(grid[0])] + grid + [["Z"] * len(grid[0])]
grid = ["".join(row) for row in grid]

sum = 0

for i in range(1, height + 1):
    for j in range(1, width + 1):
        if grid[i][j] == "A":
            word = ""

            word += grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
            word += grid[i + 1][j - 1] + grid[i][j] + grid[i - 1][j + 1]

            sum += word.count("MASMAS")
            sum += word.count("MASSAM")
            sum += word.count("SAMSAM")
            sum += word.count("SAMMAS")

print(sum)
