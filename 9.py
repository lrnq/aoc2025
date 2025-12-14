from shapely import Polygon  # noqaa

with open("9.in", "r") as f:
    lines = f.readlines()
    points = [tuple(map(int, x.split(","))) for x in lines]


ans = 0
xmax, xmin = max(x for x, y in points), min(x for x, y in points)
ymax, ymin = max(y for x, y in points), min(y for x, y in points)
for p1 in points:
    x1, y1 = p1
    for p2 in points:
        if p1 == p2:
            continue
        x2, y2 = p2
        a = abs(x2 - x1) + 1
        b = abs(y2 - y1) + 1
        ans = max(ans, a * b)
print(ans)


polygon = Polygon((x, y) for x, y in points)
squares: list[Polygon] = []
j = 0
ans = -1
for p1 in points:
    j += 1
    x1, y1 = p1
    for p2 in points:
        if p1 == p2:
            continue
        x2, y2 = p2
        r = Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])
        # I would like to find max_{r:  r covers polygon} area(r)
        if polygon.covers(r):
            # plotting.plot_polygon(r)
            # plotting.plot_polygon(polygon)
            # Picks theorem
            interior_points = r.area - r.length / 2 + 1
            ans = max(ans, interior_points + r.length)

print(int(ans))
