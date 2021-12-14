#!/usr/bin/env python3


def load():
    dots = set()
    folds = []

    with open('13.txt', 'rt') as f:
        for line in f:
            line = line.strip()

            if ',' in line:
                x, y = map(int, line.split(','))
                dots.add((x, y))

            elif 'x=' in line:
                folds.append(('x', int(line.split('=')[1])))

            elif 'y=' in line:
                folds.append(('y', int(line.split('=')[1])))

    return dots, folds


def main():
    dots, folds = load()
    #render(dots)

    for axis, pos in folds:
        fold(axis, pos, dots)

    render(dots)


def render(dots : set):
    w = max(x for x, y in dots)
    h = max(y for x, y in dots)
    for y in range(h + 1):
        for x in range(w + 1):
            print('#' if (x, y) in dots else '.', end='')
        print('')

def fold(axis : str, pos : int, dots : set):
    for x, y in dots.copy():
        if axis == 'x' and x > pos:
            distance = x - pos
            xn = x - 2 * distance
            dots.remove((x, y))
            dots.add((xn, y))

        if axis == 'y' and y > pos:
            distance = y - pos
            yn = y - 2 * distance
            dots.remove((x, y))
            dots.add((x, yn))


def do_step(word, rules):
    new_word = [word[0]]

    for (a, b) in zip(word, word[1:]):
        new_word.append(rules[(a, b)])
        new_word.append(b)

    return ''.join(new_word)


def can_visit(path, node):
    if node == 'start':
        return False
    elif is_small(node) and node in path:
        return False
    else:
        return True


def is_small(node):
    return node == node.lower()


if __name__ == '__main__':
    main()