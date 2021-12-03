lines = []
with open('./input.txt') as f:
    lines = f.readlines()

"""
index_1 = 0
index_2 = 1
index_3 = 2
index_4 = 3
curr_sum = 0
prev_sum = 99999999
times_increasing = 0

for line in lines:
    depth = int(line)
    curr_sum += depth
    index += 1

    if index % 3 == 0:
        if curr_sum > prev_sum:
            times_increasing += 1
        prev_sum = curr_sum
        curr_sum = 0

print(times_increasing)
"""

times_increasing = 0
prev_sum = 999999
for i in range(0, len(lines) - 2):
    curr_sum = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
    print(curr_sum)
    if curr_sum > prev_sum:
        times_increasing += 1
    prev_sum = curr_sum

print(times_increasing)

