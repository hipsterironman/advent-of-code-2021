contents = []
with open('/Users/ryan/develop/advent-of-code-2021/day3/input.txt') as f:
    contents = f.readlines()

# gamma_rate = ''
# epsilon_rate = ''

# for i in range(0, len(contents[0]) - 1):
#     num_0 = 0
#     num_1 = 0
#     for line in contents:
#         if line[i] == '0':
#             num_0 += 1
#         else:
#             num_1 += 1

#     if num_0 > num_1:
#         gamma_rate += '0'
#         epsilon_rate += '1'
#     else:
#         gamma_rate += '1'
#         epsilon_rate += '0'

# print(int(gamma_rate, 2) * int(epsilon_rate, 2))


def reduce_oxygen(input, i):
    num_0 = 0
    num_1 = 0
    for line in input:
        if line[i] == '0':
            num_0 += 1
        else:
            num_1 += 1

    if num_0 > num_1:
        return [line for line in input if line[i] == '0']
    else:
        return [line for line in input if line[i] == '1']


def reduce_co2(input, i):
    num_0 = 0
    num_1 = 0
    for line in input:
        if line[i] == '0':
            num_0 += 1
        else:
            num_1 += 1

    if num_0 <= num_1:
        return [line for line in input if line[i] == '0']
    else:
        return [line for line in input if line[i] == '1']


oxygen_rating = 0
oxygen_lines = contents
co2_rating = 0
co2_lines = contents
for i in range(0, len(contents[0]) - 1):
    oxygen_lines = reduce_oxygen(oxygen_lines, i)
    co2_lines = reduce_co2(co2_lines, i)
    print(co2_lines)
    if len(oxygen_lines) == 1:
        oxygen_rating = int(oxygen_lines[0], 2)

    if len(co2_lines) == 1:
        co2_rating = int(co2_lines[0], 2)

print(oxygen_rating * co2_rating)
