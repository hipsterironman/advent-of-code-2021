from pathlib import Path
contents = []
with open(str(Path(__file__).resolve().parent) + '/input.txt') as f:
    contents = f.read()[13:].split(', ')

x_min, x_max = sorted(list(map(int, contents[0][2:].split('..'))))
y_min, y_max = sorted(list(map(int, contents[1][2:].split('..'))))


def in_range(x, y):
    return x_min <= x and x <= x_max and y_min <= y and y <= y_max


def step(x_velocity, y_velocity):
    x, y = (0, 0)
    points = [(0, 0)]

    while not in_range(x, y):
        x += x_velocity
        y += y_velocity
        points.append((x, y))

        if x_velocity < 0:
            x_velocity += 1
        elif x_velocity > 0:
            x_velocity -= 1

        y_velocity -= 1

        if x > x_max or y < y_min:
            return False

    return True


def try_points():
    successful = []
    for x in range(1000):
        for y in range(-1000, 1000):
            if step(x, y):
                successful += [(x, y)]

    return successful


print(len(try_points()))
