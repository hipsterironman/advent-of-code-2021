contents = []
with open('/Users/ryan/develop/advent-of-code-2021/day6/input.txt') as f:
    contents = list(map(int, f.read().split(',')))

DAYS = 256

lanternfish = [contents.count(i) for i in range(9)]


for _ in range(DAYS):
    zero_fish = lanternfish[0]

    for i in range(8):
        lanternfish[i] = lanternfish[i + 1]

    lanternfish[6] += zero_fish
    lanternfish[8] = zero_fish


print(sum(lanternfish))

"""
from collections import deque

contents = []
with open('/Users/ryan/develop/advent-of-code-2021/day6/input.txt') as f:
    contents = list(map(int, f.read().split(',')))

DAYS = 256

lanternfish = deque([contents.count(i) for i in range(9)])


for _ in range(DAYS):
    dying_fish = lanternfish[0]
    lanternfish.rotate(-1)
    lanternfish[6] += dying_fish


print(sum(lanternfish))
"""
