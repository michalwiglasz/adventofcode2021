#!/usr/bin/env python3



with open('07.txt', 'rt') as f:
    crabs = list(map(int, f.read().strip().split(',')))

hmin = min(crabs)
hmax = max(crabs)

opt_h = None
opt_fuel = None


def calc_fuel(crab, h):
    diff = abs(crab - h)
    return diff * (diff + 1) // 2


for h in range(hmin, hmax + 1):
    fuel = sum(calc_fuel(crab, h) for crab in crabs)
    print(f"h = {h}, fuel = {fuel}")
    if opt_fuel is None or fuel < opt_fuel:
        opt_fuel = fuel
        opt_h = h

print("---")
print(f"h = {opt_h}, fuel = {opt_fuel}")
