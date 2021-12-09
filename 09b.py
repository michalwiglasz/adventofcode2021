#!/usr/bin/env python3

from functools import reduce
import numpy as np
from operator import mul
from collections import Counter


def load():
    data = []
    with open('09.txt', 'rt') as f:
        for line in f:
            data.append([int(n) for n in line.strip()])
    return np.array(data)


def main():
    data = load()

    basin_map = np.zeros_like(data)
    basin_count = 0

    for (x, y), val in np.ndenumerate(data):
        if not basin_map[x, y]:
            basin_count += 1
            find_basin([(x, y)], data, basin_map, basin_count)

    basin_sizes = Counter(b for b in basin_map.flat if b > 0)
    largest = basin_sizes.most_common(3)
    result = reduce(mul, (v for k,v in largest))
    print(result)


def find_basin(cells, data, basin_map, num):
    for x, y in cells:
        if data[x, y] == 9:
            basin_map[x, y] = -1
        elif not basin_map[x, y]:
            basin_map[x, y] = num
            neis = iter_neighbours(data.shape, x, y)
            find_basin(neis, data, basin_map, num)

def iter_neighbours(shape, x, y):
    if x > 0:
        yield x - 1, y
    if x < shape[0] - 1:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y < shape[1] - 1:
        yield x, y + 1



if __name__ == '__main__':
    main()