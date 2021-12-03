#!/usr/bin/env python3

with open('02.txt', 'rt') as f:
    input_data = f.readlines()
    input_data = [x.strip() for x in input_data]

hor = 0
depth = 0

for cmd in input_data:
    what, val = cmd.split(' ')
    val = int(val)

    if what == 'forward':
        hor += val
    elif what == 'up':
        depth -= val
    elif what == 'down':
        depth += val

mul = hor*depth
print(f"hor = {hor}, depth = {depth}, mul = {mul}")

