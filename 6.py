import functools
import numpy as np

with open("6.in", "r") as f:
    lines = [line.strip().split() for line in f.readlines()]


ans = 0
ops = lines[-1]
lines = list(zip(*lines[:-1]))
for i in range(len(lines)):
    match ops[i]:
        case "*":
            ans += functools.reduce(lambda x, y: x * y, list(map(int, lines[i])))
        case "+":
            ans += functools.reduce(lambda x, y: x + y, list(map(int, lines[i])))
print(ans)


# Reread and keep the spaces for easier slicing with numpy.
with open("6.in", "r") as f:
    grid = [list(line.strip("\n")) for line in f.readlines()][:-1]

grid = np.array(grid)
print(grid.shape)

ans = 0
tmp = None
ops_n = 0
for c in range(grid.shape[1]):
    if all(x == " " for x in grid[:, c]):
        ans += tmp
        tmp = None
        ops_n += 1
        continue
    if tmp is None:
        tmp = 1 if ops[ops_n] == "*" else 0
    num = []
    for r in range(grid.shape[0]):
        if grid[r, c] != " ":
            num.append(grid[r, c])
    res = int("".join(num))
    if ops[ops_n] == "*":
        tmp *= res
    else:
        tmp += res
print(ans + tmp)
