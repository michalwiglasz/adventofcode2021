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

DIGITS_REV = {wires: digit for digit, wires in DIGITS.items()}

displays = []

with open('08.txt', 'rt') as f:
    for line in f:
        patterns, outputs = (x.strip() for x in line.split('|'))
        patterns = set(''.join(sorted(x)) for x in patterns.split(' '))
        outputs = [''.join(sorted(x)) for x in outputs.split(' ')]
        displays.append((patterns, outputs))


def eliminate_sure(wire_candidates):
    print("--- eliminate_sure")
    sure = set()
    for cands in wire_candidates.values():
        if len(cands) == 1:
            sure |= cands

    for cands in wire_candidates.values():
        if len(cands) > 1:
            cands -= sure
    print(wire_candidates)


result = 0
for patterns, outputs in displays:

    display_digits = {}
    display_wires = {
        chr(n): None for n in range(ord('a'), ord('g')+1)
    }

    remaining_patterns = set(patterns)

    digit_candidates = {x: set() for x in range(0, 10)}
    wire_candidates = {
        chr(n): set('abcdefg') for n in range(ord('a'), ord('g')+1)
    }

    for digit, correct_wires in DIGITS.items():
        for observed_wires in patterns:
            if len(correct_wires) == len(observed_wires):
                digit_candidates[digit].add(observed_wires)
                incorrect_wires = set('abcdefg') - set(correct_wires)
                if digit in [1, 4, 7 ,8]:
                    display_digits[digit] = set(observed_wires)
                    for wire in observed_wires:
                        wire_candidates[wire] -= incorrect_wires

    # 2, 3, 5 has adg in common
    adg_cands = set.intersection(*map(set, digit_candidates[2]))
    for w in wire_candidates.keys():
        if w in adg_cands:
            wire_candidates[w] &= set('adg')
        else:
            wire_candidates[w] -= set('adg')

    # 0, 6, 9 has abfg in common
    abfg_cands = set.intersection(*map(set, digit_candidates[0]))
    for w in wire_candidates.keys():
        if w in abfg_cands:
            wire_candidates[w] &= set('abfg')
        else:
            wire_candidates[w] -= set('abfg')

    # 1 = cf
    cf_cands = display_digits[1]
    for w in wire_candidates.keys():
        if w in cf_cands:
            wire_candidates[w] &= set('cf')
        else:
            wire_candidates[w] -= set('cf')

    # 7 = 1 + a
    a_cands = set(display_digits[7]) - set(display_digits[1])
    display_wires['a'] = list(a_cands)[0]
    for w in wire_candidates.keys():
        if w in a_cands:
            wire_candidates[w] &= set('a')
        else:
            wire_candidates[w] -= set('a')

    if not all(len(x) == 1 for x in wire_candidates.values()):
        print(wire_candidates)
        exit(1)

    wire_map = {w: list(d)[0] for w, d in wire_candidates.items()}

    digit_map = {}
    for pattern in patterns:
        correct_pattern = ''.join(sorted(wire_map[w] for w in pattern))
        digit_map[pattern] = DIGITS_REV[correct_pattern]

    out_num = ''.join(str(digit_map[out]) for out in outputs)
    result += int(out_num)

print(result)




"""
    # 4 = 1 + bd
    print("--- 4 = 1 + bd")
    bd_cands = display_digits[4] - display_digits[1]
    for w in wire_candidates.keys():
        if w in bd_cands:
            wire_candidates[w] &= set('bd')
        else:
            wire_candidates[w] -= set('bd')
    print(wire_candidates)

    # 9 = 4 + a + g
    print("--- 9 = 4 + a + g")
    print(display_digits[4])
    for w, cands in wire_candidates.items():
        if 'g' in cands:
            cand_9 = display_digits[4] | set(display_wires['a']) | set(w)
            print(cand_9)
            if len(cand_9) != len(DIGITS[9]):
                cands.remove('g')
    print(wire_candidates)
    eliminate_sure(wire_candidates)

    # 9 = 8 - e
    print("--- 9 = 8 - e")
    e_cands = set()
    for pattern in digit_candidates[9]:
        e_wire = display_digits[8] - set(pattern)
        e_cands |= (e_wire)
    print(e_cands)
    for w in wire_candidates.keys():
        if w not in e_cands:
            wire_candidates[w] -= set('e')
    print(wire_candidates)
    eliminate_sure(wire_candidates)
"""

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