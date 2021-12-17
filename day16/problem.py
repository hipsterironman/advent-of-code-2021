from pathlib import Path
from math import prod
contents = []
with open(str(Path(__file__).resolve().parent) + '/input.txt') as f:
    contents = f.read()


PARSE_HEX = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

binary = ''
for char in contents:
    binary += PARSE_HEX[char]

version_sums = 0


def parse(input):
    global version_sums
    packet_version = int(input[:3], 2)
    version_sums += packet_version
    packet_id = int(input[3:6], 2)
    input = input[6:]

    if packet_id == 4:
        num = ''
        while True:
            num += input[1:5]
            cnt = input[0]
            input = input[5:]
            if cnt == '0':
                break
        return (input, int(num, 2))

    else:
        type_id = int(input[0])
        input = input[1:]
        answer = []

        if type_id == 0:
            packets_length = int(input[:15], 2)
            input = input[15:]
            subpackets = input[:packets_length]
            while subpackets:
                s, ugh = parse(subpackets)
                subpackets = s
                answer.append(ugh)
            input = input[packets_length:]
        elif type_id == 1:
            packets_num = int(input[:11], 2)
            input = input[11:]
            for _ in range(packets_num):
                s, ugh = parse(input)
                input = s
                answer.append(ugh)

        if packet_id == 0:
            return (input, sum(answer))
        elif packet_id == 1:
            return (input, prod(answer))
        elif packet_id == 2:
            return (input, min(answer))
        elif packet_id == 3:
            return (input, max(answer))
        elif packet_id == 5:
            return (input, 1) if answer[0] > answer[1] else (input, 0)
        elif packet_id == 6:
            return (input, 1) if answer[0] < answer[1] else (input, 0)
        elif packet_id == 7:
            return (input, 1) if answer[0] == answer[1] else (input, 0)


print(parse(binary))
