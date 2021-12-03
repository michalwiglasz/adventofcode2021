#!/usr/bin/env python3

with open('01.txt', 'rt') as f:
    numbers = f.readlines()
    numbers = [int(x.strip()) for x in numbers]

prev = None
incr = 0

for num in numbers:
    if prev is not None:
        if num > prev:
            incr += 1
    prev = num

print(incr)