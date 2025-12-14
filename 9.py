from shapely import Polygon  # noqaa

with open("9.in", "r") as f:
    lines = f.readlines()
    points = [tuple(map(int, x.split(","))) for x in lines]


ans = 0
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
ans = 0
for p1 in points:
    x1, y1 = p1
    for p2 in points:
        if p1 == p2:
            continue
        x2, y2 = p2
        poly = Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])
        # poly is now a rectangle. I would like to find max_{poly covers polygon} area(poly)
        if polygon.covers(poly):
            # Picks theorem :) Using the same simple method as in part 1 is enough too...
            interior_points = poly.area - poly.length / 2 + 1
            ans = max(ans, interior_points + poly.length)
print(int(ans))
