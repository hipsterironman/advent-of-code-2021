from pathlib import Path
from heapq import heappop, heappush
with open(str(Path(__file__).resolve().parent) + '/input.txt') as f:
    contents = [list(map(int, line)) for line in f.read().strip().split('\n')]

END = (5 * (len(contents)) - 1, 5 * (len(contents[0])) - 1)

heap = [(0, 0, 0)]
visited = {(0, 0)}
while heap:
    distance, x, y = heappop(heap)
    if (x, y) == END:
        print(distance)
        break

    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        x_, y_ = x + dx, y + dy
        # if 0 <= x_ < len(contents) and 0 <= y_ < len(contents[0]):
        if x_ < 0 or y_ < 0 or x_ >= 5 * len(contents) or y_ >= 5 * len(contents):
            continue

        a, am = divmod(x_, len(contents))
        b, bm = divmod(y_, len(contents[0]))
        n = ((contents[am][bm] + a + b) - 1) % 9 + 1

        if (x_, y_) not in visited:
            visited.add((x_, y_))
            heappush(heap, (distance + n, x_, y_))


# points = {}
# for x in range(len(contents)):
#     for y in range(len(contents[x])):
#         points[(x, y)] = int(contents[x][y])


# def check_adjacent(x, y):
#     possibles = {}
#     if (x + 1, y) in points:
#         possibles[(x + 1, y)] = points[(x + 1, y)]
#     if (x - 1, y) in points:
#         possibles[(x - 1, y)] = points[(x - 1, y)]
#     if (x, y + 1) in points:
#         possibles[(x, y + 1)] = points[(x, y + 1)]
#     if (x, y - 1) in points:
#         possibles[(x, y - 1)] = points[(x, y - 1)]

#     # return min(possibles, key=possibles.get)
#     min_val = min(possibles.values())
#     return [key for key in possibles.keys() if possibles[key] == min_val]


# print(check_adjacent(*START))
