crabs = []
with open('/Users/ryan/develop/advent-of-code-2021/day7/input.txt') as f:
    crabs = list(map(int, f.read().split(',')))

min_x = min(crabs)
max_x = max(crabs)

fuels = []
for i in range(min_x, max_x + 1):
    fuels.append(sum((abs(n - i) * (abs(n - i) + 1)) / 2 for n in crabs))

print(min(fuels))
