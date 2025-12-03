with open("3.in", "r") as f:
    lines = f.readlines()

lines = [list(map(int, list(x.strip()))) for x in lines]


def f(nums, start, rem):
    if not rem:
        return []
    end = len(nums) - rem + 1
    mx = max(nums[start:end])
    return [mx] + f(nums, nums.index(mx, start, end) + 1, rem - 1)


ans_1, ans_2 = 0, 0
for line in lines:
    ans_1 += int("".join(list(map(str, f(line, 0, 2)))))
    ans_2 += int("".join(list(map(str, f(line, 0, 12)))))

print("Part 1:", ans_1)
print("Part 2:", ans_2)
