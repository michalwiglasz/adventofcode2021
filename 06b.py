#!/usr/bin/env python3


from collections import Counter


with open('06.txt', 'rt') as f:
    fishes = Counter(map(int, f.read().strip().split(',')))

for day in range(256):
    new_fishes = Counter({age - 1: cnt for age, cnt in fishes.items()})
    new_fishes[8] += new_fishes[-1]
    new_fishes[6] += new_fishes[-1]
    del new_fishes[-1]
    fishes = new_fishes
    print(f"Day {day+1}: {sum(fishes.values())} fish")
