#!/usr/bin/env python3

from pprint import pprint

DIGITS = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}

displays = []

with open('08.txt', 'rt') as f:
    for line in f:
        patterns, outputs = (x.strip() for x in line.split('|'))
        patterns = [''.join(sorted(x)) for x in patterns.split(' ')]
        outputs = [''.join(sorted(x)) for x in outputs.split(' ')]
        displays.append((patterns, outputs))


count = 0
for patterns, outputs in displays:

    for n in [1, 4, 7, 8]:
        count += sum(1 for out in outputs if len(out) == len(DIGITS[n]))

print(count)
