from pathlib import Path
from collections import defaultdict
contents = []
with open(str(Path(__file__).resolve().parent) + '/input.txt') as f:
    contents = f.read().split('\n')

raw_folds = contents[-12:]
raw_points = contents[:-13]

folds = []
for fold in raw_folds:
    dimension, val = fold[11:].split('=')
    folds += [(dimension, int(val))]

points = []
for point in raw_points:
    x, y = point.split(',')
    points += [(int(x), int(y))]

grid_points = defaultdict(int)

for point in points:
    grid_points[point] = 1

for fold in folds:
    dimension, val = fold
    for point in points:
        x, y = point
        if dimension == 'x':
            if x > val:
                differential = val - (x - val)
                grid_points[(differential, y)] = 1
                grid_points[point] = 0
        else:
            if y > val:
                differential = y - val
                grid_points[(x, val - differential)] = 1
                grid_points[point] = 0

    points = [point for point in grid_points.keys() if grid_points[point] == 1]

max_x = max(x for x, _ in points)
max_y = max(y for _, y in points)

output = []
for i in range(max_y + 1):
    line = []
    for j in range(max_x + 1):
        line.append('-')
    output.append(line)

for i in range(max_x + 1):
    for j in range(max_y + 1):
        if (i, j) in points:
            output[j][i] = '#'
        else:
            output[j][i] = '-'

for line in output:
    print(line)
