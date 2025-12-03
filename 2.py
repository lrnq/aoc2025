with open("2.in", "r") as f:
    lines = f.readlines()

line = lines[0]
ranges = line.split(",")


def get_repeated_substring(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            candidate = s[:i]
            if candidate * (n // i) == s:
                return candidate
    return None


c = 0
for _range in ranges:
    i, j = _range.split("-")
    i, j = int(i), int(j)
    print(i, j)
    for x in range(i, j + 1):
        cc = get_repeated_substring(str(x))
        if cc is not None:
            c += x
print(c)
