with open("3.in", "r") as f:
    lines = f.readlines()

lines = [list(map(int, list(x.strip()))) for x in lines]


def f(nums, start, end, acc, target):
    if len(acc) == target:
        return acc
    mx, mx_idx = -1, -1
    for i in range(start, len(nums) - end + 1):
        if nums[i] > mx:
            mx, mx_idx = nums[i], i
    acc.append(mx)
    return f(nums, mx_idx + 1, end - 1, acc, target)


ans_1 = 0
ans_2 = 0
for line in lines:
    ans_1 += int("".join(list(map(str, f(line, 0, 2, [], 2)))))
    ans_2 += int("".join(list(map(str, f(line, 0, 12, [], 12)))))
print("Part 1:", ans_1)
print("Part 2:", ans_2)
