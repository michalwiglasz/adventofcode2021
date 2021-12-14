#!/usr/bin/env python3

from pprint import pprint
from collections import Counter


def load():
    rules = {}
    with open('14.txt', 'rt') as f:
        template = f.readline().strip()

        for line in (ln.strip() for ln in f if ln.strip()):
            left, right = line.split(' -> ')
            rules[tuple(left)] = right
    return template, rules


def main():
    word, rules = load()

    chars = Counter(word)
    pairs = Counter(zip(word, word[1:]))
    #print(0, end=' ')
    #pprint(chars)

    for i in range(40):
        do_step(chars, pairs, rules)
        #print(i+1, end=' ')
        #pprint(chars)

    most = chars.most_common()[0][1]
    least = chars.most_common()[-1][1]
    print(most - least)


def do_step(chars : Counter, pairs : Counter, rules : dict):
    for (a, b), cnt in pairs.copy().items():
        y = rules[(a, b)]
        pairs[(a, b)] -= cnt
        pairs[(a, y)] += cnt
        pairs[(y, b)] += cnt
        chars[y] += cnt


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