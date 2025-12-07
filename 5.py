with open("5.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]


ranges = []
for i, l in enumerate(lines):
    if l == "": break
    ranges.append(tuple(map(int, l.split("-"))))

ingredients = list(map(int, lines[i + 1 :]))


ans = 0
for x in ingredients:
    state = 0
    for left, right in ranges:
        if left <= x <= right:
            state = 0
            break
        else:
            state = 1
    ans += state == 0

print(ans)

ans2 = 0
ranges.sort()
cur_start, cur_end = ranges[0]
for start, end in ranges[1:]:
    if start > cur_end:
        ans2 += cur_end - cur_start + 1
        cur_start = start
    cur_end = max(cur_end, end)

ans2 += cur_end - cur_start + 1
print(ans2)
