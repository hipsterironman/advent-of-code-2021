from pathlib import Path
from collections import defaultdict

contents = []
with open(str(Path(__file__).resolve().parent) + '/input.txt') as f:
    contents = f.read().split('\n')

connections = defaultdict(lambda: [])
for line in contents:
    first, second = line.split('-')
    connections[first].append(second)
    connections[second].append(first)


def check_visited(visited, curr):
    return curr not in visited or all(visited.count(cave) != 2 for cave in visited)


def follow_path(curr, visited):
    if curr == 'end':
        return 1

    if not check_visited(visited, curr):
        return 0

    if curr.islower():
        visited.append(curr)

    return sum(follow_path(cave, visited.copy())
               for cave in connections[curr] if cave != 'start')


print(follow_path('start', []))
