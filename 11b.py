#!/usr/bin/env python3

import itertools
import numpy as np


def load():
    data = []
    with open('11.txt', 'rt') as f:
        for line in f:
            data.append([int(n) for n in line.strip()])
    return np.array(data)


def main():
    data = load()

    for step in itertools.count(1):
        num_flashes = do_step(data)
        if num_flashes == data.size:
            print(step)
            break


def do_step(data : np.array):
    # First, the energy level of each octopus increases by 1.
    data += 1

    # Then, any octopus with an energy level greater than 9 flashes.
    should_continue = True
    flash_map = np.zeros_like(data, dtype=bool)
    while should_continue:
        should_continue = False
        for (x, y), val in np.ndenumerate(data):
            if val > 9 and not flash_map[x, y]:
                do_flash(data, x, y)
                should_continue = True
                flash_map[x, y] = True

    num_flashes = flash_map.sum()

    # Finally, any octopus that flashed during this step has its energy level set to 0
    data[data > 9] = 0
    return num_flashes


def do_flash(data : np.array, x, y):
    for nx, ny in iter_neighbours(data.shape, x, y):
        data[nx, ny] += 1


def iter_neighbours(shape, x, y):
    neighs = set()
    for nx in range(max(x - 1, 0), min(x + 2, shape[0])):
        for ny in range(max(y - 1, 0), min(y + 2, shape[1])):
            neighs.add((nx, ny))
    #neighs.remove((x, y))
    return neighs


if __name__ == '__main__':
    main()