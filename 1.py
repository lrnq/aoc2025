with open("1.in", "r") as f:
    lines = f.readlines()

ans = 0
pos = 50
for l in lines:
    x = 0
    sign = l[0]
    t = int(l[1:])
    for x in range(abs(t)):
        if sign == "L":
            pos -= 1
        else:
            pos += 1
        if (pos % 100) == 0:
            ans += 1
print(ans)
