#!/usr/bin/env python3

with open('01.txt', 'rt') as f:
    numbers = f.readlines()
    numbers = [int(x.strip()) for x in numbers]

prev = None
incr = 0

window_size = 3

for i in range(len(numbers) - window_size + 1):
    a = numbers[i: i + window_size]
    b = numbers[i+1: i+1 + window_size]

    if len(a) == window_size and len(b) == window_size and sum(b) > sum(a):
        incr += 1

print(incr)

