contents = []
with open('./input.txt') as f:
    contents = f.readlines()

gamma_rate = ''
epsilon_rate = ''

for i in range(0, len(contents[0]) - 1):
    num_0 = 0
    num_1 = 0
    for line in contents:
        if line[i] == '0':
            num_0 += 1
        else:
            num_1 += 1

    if num_0 > num_1:
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

oxygen_rating = ''
co2_rating = ''

for i in range(0, len(contents[0]) - 1):
    num_0 = 0
    num_1 = 0
    for line in contents:
        if line[i] == '0':
            num_0 += 1
        else:
            num_1 += 1

    if num_0 > num_1:


