from itertools import count

with open("4.in", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

n, m = len(lines), len(lines[0])
adj8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def state(lines):
    return "".join(["".join(line) for line in lines])


for x in 1, 2:
    ans = 0
    s = None
    for q in count():
        if ((x == 1) and q) or (state(lines) == s):
            break
        s = state(lines)
        for i in range(n):
            for j in range(m):
                if lines[i][j] != "@":
                    continue
                cnt = 0
                for dx, dy in adj8:
                    if 0 <= i + dx < n and 0 <= j + dy < m:
                        cnt += lines[i + dx][j + dy] == "@"
                if cnt < 4:
                    ans += 1
                    if x == 2:
                        lines[i][j] = "."
        # for line in lines:
        #    print(line)

    print(ans)
