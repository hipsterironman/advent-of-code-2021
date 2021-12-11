from pathlib import Path
octopi_input = []
with open(str(Path(__file__).resolve().parent) + '/input.txt') as f:
    octopi_input = f.read().split('\n')

octopi = {}
for i, line in enumerate(octopi_input):
    for j, octopus in enumerate(line):
        octopi[(i, j)] = int(octopus)


def find_adjacent(coord):
    i, j = coord
    return [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1),
            (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]


def flash_adjacent(coord, octopi, flashed):
    queue = find_adjacent(coord)
    while queue:
        curr = queue.pop(0)
        if curr in octopi and curr not in flashed:
            octopi[curr] += 1
            if octopi[curr] > 9:
                flashed.append(curr)
                queue.extend(find_adjacent(curr))

    return flashed


flash_count = 0
for i in range(100):
    flashed = []
    for coord in octopi:
        octopi[coord] += 1
        if octopi[coord] > 9 and coord not in flashed:
            flashed.append(coord)
            flashed = flash_adjacent(coord, octopi, flashed)

    flash_count += len(flashed)

    for coord in octopi:
        if octopi[coord] > 9:
            octopi[coord] = 0

    # part 2
    if all(octopi[coord] == 0 for coord in octopi):
        print(i + 1)
        break

# part 1
print(flash_count)
