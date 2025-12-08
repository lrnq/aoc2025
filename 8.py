from collections import Counter
from math import prod

with open("8.in", "r") as f:
    lines = f.readlines()
    points = [list(map(int, x.split(","))) for x in lines]


def d(p1, p2):
    return sum((x1 - x2) ** 2 for x1, x2 in zip(p1, p2))


class DSU:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = list(range(n))

    def find(self, i):
        root = self.parent[i]

        if self.parent[root] != root:
            self.parent[i] = self.find(root)
            return self.parent[i]

        return root

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[y_root] < self.rank[x_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


distances = []
for i, p1 in enumerate(points):
    for j, p2 in enumerate(points):
        if i >= j:
            continue
        distances.append((d(p1, p2), i, j))

distances.sort()
clusters = DSU(len(points))
for dd, i, j in distances[:1000]:
    clusters.union(i, j)
print(prod([x[0] for x in Counter(clusters.parent).most_common(3)]))


for dd, i, j in distances[1000:]:
    clusters.union(i, j)
    if len(Counter(clusters.parent)) == 1:
        print(points[i][0] * points[j][0])
        break
