#!/usr/bin/env python3

from pprint import pprint
from collections import Counter


def load():
    with open('05.txt', 'rt') as f:
        for line in f:
            start, end = line.strip().split(' -> ')
            start = tuple(map(int, start.split(',')))
            end = tuple(map(int, end.split(',')))
            yield start, end


def add_line(counter, line):
    start, end = line

    if start > end:
        start, end = end, start

    x1, x2 = start[0], end[0]
    y1, y2 = start[1], end[1]

    dx = 1 if x1 < x2 else -1
    dy = 1 if y1 < y2 else -1

    x = x1
    y = y1

    while True:
        counter[(x, y)] += 1

        if x == x2 and y == y2:
            break

        if x != x2:
            x += dx
        if y != y2:
            y += dy


def print_diagram(counter):
    max_x = max(p[0] for line in lines for p in line)
    max_y = max(p[1] for line in lines for p in line)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            n = counter[(x,y)]
            print(n or '.', end="")
        print()

lines = list(load())
diagram = Counter()

for line in lines:
    add_line(diagram, line)

#print_diagram(diagram)

overlaps = filter(lambda n: n > 1, diagram.values())
print(sum(1 for _ in overlaps))