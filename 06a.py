#!/usr/bin/env python3


with open('06.txt', 'rt') as f:
    fishes = map(int, f.read().strip().split(','))



for day in range(80):
    fishes = [f - 1 for f in fishes]
    new = sum(1 for f in fishes if f < 0)
    fishes = [f if f >= 0 else 6 for f in fishes] + [8] * new
    print(f"Day {day+1}: {len(fishes)} fish")
