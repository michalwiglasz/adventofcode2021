#!/usr/bin/env python3

with open('01.txt', 'rt') as f:
    numbers = f.readlines()
    numbers = [int(x.strip()) for x in numbers]

prev = None
incr = 0

window_size = 3
window_step = 1

from collections import deque

d = deque(maxlen=window_size+window_step)

for i, num in enumerate(numbers):
    d.append(num)
    w1 = list(d)[:window_size]
    w2 = list(d)[-window_size:]

    if len(d) == d.maxlen and sum(w2) > sum(w1):
        incr += 1

print(incr)

