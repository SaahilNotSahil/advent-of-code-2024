with open("input.txt", "r") as f:
    lines = f.readlines()

grid = [list(line.strip()) for line in lines]

height = len(grid)
width = len(grid[0])

for i in range(height):
    grid[i] = ["Z"] * 3 + grid[i] + ["Z"] * 3

grid = [["Z"] * len(grid[0])] * 3 + grid + [["Z"] * len(grid[0])] * 3
grid = ["".join(row) for row in grid]

sum = 0

for i in range(3, height + 3):
    for j in range(3, width + 3):
        if grid[i][j] == "X":
            word = ""

            word += grid[i][j : j + 4]
            word += (
                grid[i][j]
                + grid[i + 1][j + 1]
                + grid[i + 2][j + 2]
                + grid[i + 3][j + 3]
            )
            word += (
                grid[i][j] + grid[i + 1][j] + grid[i + 2][j] + grid[i + 3][j]
            )
            word += (
                grid[i][j]
                + grid[i + 1][j - 1]
                + grid[i + 2][j - 2]
                + grid[i + 3][j - 3]
            )
            word += (
                grid[i][j] + grid[i][j - 1] + grid[i][j - 2] + grid[i][j - 3]
            )
            word += (
                grid[i][j]
                + grid[i - 1][j - 1]
                + grid[i - 2][j - 2]
                + grid[i - 3][j - 3]
            )
            word += (
                grid[i][j] + grid[i - 1][j] + grid[i - 2][j] + grid[i - 3][j]
            )
            word += (
                grid[i][j]
                + grid[i - 1][j + 1]
                + grid[i - 2][j + 2]
                + grid[i - 3][j + 3]
            )

            sum += word.count("XMAS")

print(sum)
