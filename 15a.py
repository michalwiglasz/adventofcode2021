#!/usr/bin/env python3

import numpy as np



def load():
    data = []
    with open('15.txt', 'rt') as f:
        for line in f:
            data.append([int(n) for n in line.strip()])
    return np.array(data)


def main():
    risk_map = load()

    dest = tuple(n-1 for n in risk_map.shape)
    distance = np.full_like(risk_map, 1e9)
    previous = np.empty_like(risk_map, dtype=tuple)

    distance[0, 0] = 0
    unvisited = set(np.ndindex(risk_map.shape))

    while unvisited:
        minx, miny, minval = min(((x, y, distance[x, y]) for x, y in unvisited), key=lambda t: t[2])
        if (minx, miny) == dest:
            break
        for x, y in iter_neighbours(risk_map.shape, minx, miny):
            d = minval + risk_map[x, y]
            if d < distance[x, y]:
                distance[x, y] = d
                previous[x, y] = (x, y)
        unvisited.remove((minx, miny))

    #print(distance)
    print(distance[dest])


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