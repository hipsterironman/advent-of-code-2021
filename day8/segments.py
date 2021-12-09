segments_input = []
with open('/Users/ryan/develop/advent-of-code-2021/day8/input.txt') as f:
    segments_input = f.read().split('\n')

ONE_OUTPUT_SEGMENTS = 2
FOUR_OUTPUT_SEGMENTS = 4
SEVEN_OUTPUT_SEGMENTS = 3
EIGHT_OUTPUT_SEGMENTS = 7

unique_output_segments = {
    ONE_OUTPUT_SEGMENTS: 1,
    FOUR_OUTPUT_SEGMENTS: 4,
    SEVEN_OUTPUT_SEGMENTS: 7,
    EIGHT_OUTPUT_SEGMENTS: 8
}

patterns = []
outputs = []
for line in segments_input:
    pattern, output = line.split(' | ')
    patterns.append(pattern.split(' '))
    outputs.append(output.split(' '))

# part one
digit_count = 0
for output in outputs:
    curr_converted_ouput = []
    for num in output:
        if len(num) in unique_output_segments:
            digit_count += 1

print(digit_count)

# part two


def check_string(str, chars):
    return all([character in chars for character in str])


final_sum = 0
for i in range(0, len(patterns)):
    curr_pattern = []
    unique_patterns = {}
    for num in patterns[i]:
        if len(num) in unique_output_segments:
            curr_pattern.append(unique_output_segments[len(num)])
            unique_patterns[unique_output_segments[len(num)]] = num
        else:
            curr_pattern.append(num)

    fourdiff = unique_patterns[4]
    for letter in unique_patterns[1]:
        fourdiff = fourdiff.replace(letter, '')

    for pattern in curr_pattern:
        if type(pattern) is int:
            continue

        if len(pattern) == 5:
            if check_string(unique_patterns[1], pattern):
                unique_patterns[3] = pattern
            elif check_string(fourdiff, pattern):
                unique_patterns[5] = pattern
            else:
                unique_patterns[2] = pattern
        elif len(pattern) == 6:
            if check_string(unique_patterns[4], pattern):
                unique_patterns[9] = pattern
            elif check_string(fourdiff, pattern):
                unique_patterns[6] = pattern
            else:
                unique_patterns[0] = pattern

    converter = dict((v, k) for (k, v) in unique_patterns.items())

    final_conversion = ''
    for num in outputs[i]:
        for key in converter:
            if sorted(key) == sorted(num):
                final_conversion += str(converter[key])

    final_sum += int(final_conversion)

print(final_sum)
