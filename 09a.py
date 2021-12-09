#!/usr/bin/env python3


def load():
    data = []
    with open('09.txt', 'rt') as f:
        for line in f:
            data.append([int(n) for n in line.strip()])
    return data


def main():
    data = load()
    h = len(data)
    w = len(data[0])

    risk_levels = 0

    for x in range(len(data)):
        for y in range(len(data[0])):
            cell = data[x][y]
            if all(n > cell for n in iter_neighbours(data, x, y)):
                risk_levels += 1 + cell

    print(risk_levels)


def iter_neighbours(data, x, y):
    h = len(data)
    w = len(data[0])

    if x > 0:
        yield data[x - 1][y]
    if x < h - 1:
        yield data[x + 1][y]
    if y > 0:
        yield data[x][y - 1]
    if y < w - 1:
        yield data[x][y + 1]



if __name__ == '__main__':
    main()