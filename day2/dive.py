import re

contents = []
with open('./input.txt') as f:
    contents = f.readlines()

DIVE_REGEX = r'(forward|down|up) (\d+)'

def parse_line(input):
    direction, length = re.search(DIVE_REGEX, input).groups()
    return (direction, length)

horizontal = 0
depth = 0
aim = 0
for line in contents:
    direction, length = parse_line(line)
    if direction == 'forward':
        horizontal += int(length)
        depth += aim * int(length)
    elif direction == 'up':
        aim -= int(length)
    elif direction == 'down':
        aim += int(length)

print(horizontal * depth)

