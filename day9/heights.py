from math import prod

heights_input = []
with open('/Users/ryan/develop/advent-of-code-2021/day9/input.txt') as f:
    heights_input = f.read().split('\n')

heights = [list(map(int, (num for num in line))) for line in heights_input]


def check_adjacent(i, j, points):
    results = []
    if not i - 1 < 0:
        results.append(points[i][j] < points[i - 1][j])
    if not i + 1 >= len(points):
        results.append(points[i][j] < points[i + 1][j])
    if not j - 1 < 0:
        results.append(points[i][j] < points[i][j - 1])
    if not j + 1 >= len(points[i]):
        results.append(points[i][j] < points[i][j + 1])

    return all(results)


low_points = 0
low_point_locations = []
for i in range(len(heights)):
    for j in range(len(heights[i])):
        if check_adjacent(i, j, heights):
            low_points += heights[i][j] + 1
            low_point_locations.append((i, j))

print(low_points)


def measure_basin(i, j, points, visited):
    if (i >= len(points) or i < 0 or j >= len(points[i]) or j < 0
            or (i, j) in visited or points[i][j] == 9):
        return 0

    visited.append((i, j))

    return (1 + measure_basin(i + 1, j, points, visited)
            + measure_basin(i - 1, j, points, visited)
            + measure_basin(i, j + 1, points, visited)
            + measure_basin(i, j - 1, points, visited))


basin_sizes = [measure_basin(i, j, heights, [])
               for i, j in low_point_locations]
print(prod(sorted(basin_sizes)[-3:]))
