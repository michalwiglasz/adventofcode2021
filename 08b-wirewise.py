#!/usr/bin/env python3

import random
import itertools

from pprint import pprint
from collections import defaultdict


WIRES = set('abcdefg')
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

# [('e', {0, 8, 2, 6}),
#  ('b', {0, 4, 5, 6, 8, 9}),
#  ('d', {2, 3, 4, 5, 6, 8, 9}),
#  ('g', {0, 2, 3, 5, 6, 8, 9}),
#  ('a', {0, 2, 3, 5, 6, 7, 8, 9}),
#  ('c', {0, 1, 2, 3, 4, 7, 8, 9}),
#  ('f', {0, 1, 3, 4, 5, 6, 7, 8, 9})]

WIRES = {
    w: set(digit for digit, wires in DIGITS.items() if w in wires)
    for w in 'abcdefg'
}
DIGITS_REV = {wires: digit for digit, wires in DIGITS.items()}

displays = []

with open('08.txt', 'rt') as f:
    for line in f:
        patterns, outputs = (x.strip() for x in line.split('|'))
        patterns = set(''.join(sorted(x)) for x in patterns.split(' '))
        outputs = [''.join(sorted(x)) for x in outputs.split(' ')]
        displays.append((patterns, outputs))

result = 0
for patterns, outputs in displays:

    display_digits = {}
    display_wires = {
        chr(n): None for n in range(ord('a'), ord('g')+1)
    }

    wire_patterns = {w: set() for w in 'abcdefg'}

    for pattern in patterns:
        for pattern_wire in pattern:
            wire_patterns[pattern_wire].add(pattern)


    wire_map = {w: set() for w in 'abcdefg'}

    for correct_wire, correct_digits in WIRES.items():
        for obs_wire, obs_patterns in wire_patterns.items():
            if len(correct_digits) == len(obs_patterns):
                wire_map[obs_wire].add(correct_wire)

    # only wires with non-unique digits count is D/G and A/C:
    # d vs g: d is used in 4
    # a vs c: c is used in 4

    pattern_4 = dict()
    for pattern in patterns:
        if len(pattern) == len(DIGITS[4]):
            pattern_4 = pattern


    for wire, cands in wire_map.items():
        if cands == set('dg'):
            if pattern_4 in wire_patterns[wire]:
                cands.remove('g')
            else:
                cands.remove('d')
        elif cands == set('ac'):
            if pattern_4 in wire_patterns[wire]:
                cands.remove('a')
            else:
                cands.remove('c')

    wire_map = {w: list(d)[0] for w, d in wire_map.items()}

    digit_map = {}
    for pattern in patterns:
        correct_pattern = ''.join(sorted(wire_map[w] for w in pattern))
        digit_map[pattern] = DIGITS_REV[correct_pattern]

    out_num = ''.join(str(digit_map[out]) for out in outputs)
    result += int(out_num)

print(result)

#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc

# a=c
# b=f
# c=g
# d=a
# e=b
# f=d
# g=e