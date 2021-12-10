from pathlib import Path
syntax_input = []
with open(str(Path(__file__).resolve().parent) + '/input.txt') as f:
    syntax_input = f.read().split('\n')

MATCHING_PAIR = {
    ')': '(',
    '}': '{',
    '>': '<',
    ']': '['
}

POINTS_TABLE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    '': 0
}

FINISH_POINTS = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}


def process_char(char, stack):
    if char == '(' or char == '{' or char == '<' or char == '[':
        stack.append(char)
    elif stack[-1] == MATCHING_PAIR[char]:
        stack.pop()
    else:
        return False

    return True


def finish_line(stack):
    score = 0
    while len(stack) != 0:
        score *= 5
        char = stack.pop()
        score += FINISH_POINTS[char]

    return score


def process_line(line):
    stack = []
    for char in line:
        if not process_char(char, stack):
            return char

    if len(stack) != 0:
        return finish_line(stack)

    return ''


illegal_sum = 0
fixed_scores = []
for line in syntax_input:
    res = process_line(line)

    if type(res) is int:
        fixed_scores.append(res)
    else:
        illegal_sum += POINTS_TABLE[res]

print(illegal_sum)
print(len(fixed_scores) // 2)
print(sorted(fixed_scores)[len(fixed_scores) // 2])
