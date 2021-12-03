#!/usr/bin/env python3

with open('03.txt', 'rt') as f:
    input_data = f.readlines()
    input_data = [x.strip() for x in input_data]


from collections import defaultdict, Counter

counters = defaultdict(Counter)

for line in input_data:

    for pos, num in enumerate(line):
        counters[pos][num] += 1


gam = ''
eps = ''
for pos, cnt in sorted(counters.items()):
    common = cnt.most_common()
    gam += common[0][0]
    eps += common[1][0]

gam = int(gam, 2)
eps = int(eps, 2)

mul = gam*eps
print(f"gam = {gam}, eps = {eps}, mul = {mul}")

