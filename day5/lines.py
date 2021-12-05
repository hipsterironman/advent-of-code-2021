contents = []
with open('/Users/ryan/develop/advent-of-code-2021/day5/input.txt') as f:
    contents = f.read().split('\n')

grid = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]

for line in contents:
    coord1, coord2 = line.split(' -> ')
    x1, y1 = map(int, coord1.split(','))
    x2, y2 = map(int, coord2.split(','))

    if x1 != x2 and y1 != y2:
        if x2 > x1 and y2 > y1:
            for i in range(0, x2 - x1 + 1):
                grid[y1 + i][x1 + i] += 1
        elif x2 > x1 and y2 < y1:
            for i in range(0, x2 - x1 + 1):
                grid[y1 - i][x1 + i] += 1
        elif x2 < x1 and y2 > y1:
            for i in range(0, x1 - x2 + 1):
                grid[y1 + i][x1 - i] += 1
        elif x2 < x1 and y2 < y1:
            for i in range(0, x1 - x2 + 1):
                grid[y1 - i][x1 - i] += 1
    else:
        if x2 > x1:
            for x in range(x1, x2 + 1):
                grid[y1][x] += 1
        elif x2 < x1:
            for x in range(x2, x1 + 1):
                grid[y1][x] += 1
        elif y2 > y1:
            for y in range(y1, y2 + 1):
                grid[y][x1] += 1
        elif y2 < y1:
            for y in range(y2, y1 + 1):
                grid[y][x1] += 1


for line in grid:
    print(line)

print(sum(sum(1 for val in row if val >= 2) for row in grid))
