with open("7.in", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]


n, m = len(lines), len(lines[0])
beams = [(0, lines[0].index("S"))]
splits = set()
for i in range(n):
    new_beams_split = set()
    new_beams_move = set()
    for ii, jj in beams:
        if 0 <= ii + 1 < n:
            if lines[ii + 1][jj] == "^":
                splits.add((ii + 1, jj))
                if 0 <= jj + 1 < m:
                    new_beams_split.add((ii + 1, jj + 1))
                if 0 <= jj - 1 < m:
                    new_beams_split.add((ii + 1, jj - 1))
            else:
                new_beams_move.add((ii + 1, jj))
    beams = new_beams_split | new_beams_move

print(len(splits))

dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][lines[0].index("S")] = 1
for i in range(n - 1):
    for j in range(m):
        if lines[i + 1][j] != "^":
            dp[i + 1][j] += dp[i][j]
        else:
            if 0 <= j + 1 < m:
                dp[i + 1][j + 1] += dp[i][j]
            if 0 <= j - 1 < m:
                dp[i + 1][j - 1] += dp[i][j]
print(sum(dp[-1][x] for x in range(m)))
