from pathlib import Path
from collections import defaultdict, Counter
contents = []
with open(str(Path(__file__).resolve().parent) + '/input.txt') as f:
    contents = f.read().split('\n')

polymer = contents[0]
raw_pair_insertions = map(lambda line: line.split(' -> '), contents[2:])

pair_insertions = defaultdict(str)
for couple, element in raw_pair_insertions:
    pair_insertions[couple] = element

pairs_count = defaultdict(int)
for i in range(len(polymer) - 1):
    pairs_count[polymer[i:i + 2]] += 1

chars_count = defaultdict(int)
for char in polymer:
    chars_count[char] += 1

for _ in range(40):
    for (char1, char2), num in pairs_count.copy().items():
        new_char = pair_insertions[char1 + char2]
        pairs_count[char1 + new_char] += num
        pairs_count[new_char + char2] += num
        chars_count[new_char] += num
        pairs_count[char1 + char2] -= num


print(max(chars_count.values()) - min(chars_count.values()))
