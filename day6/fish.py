from collections import deque

contents = []
with open('/Users/ryan/develop/advent-of-code-2021/day6/input.txt') as f:
    contents = list(map(int, f.read().split(',')))

DAYS = 256
lanternfish = deque([contents.count(i) for i in range(9)])

for _ in range(DAYS):
    lanternfish.rotate(-1)
    lanternfish[6] += lanternfish[-1]

print(sum(lanternfish))
