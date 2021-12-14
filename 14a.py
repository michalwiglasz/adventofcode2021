#!/usr/bin/env python3

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
    #print(0, word)

    for i in range(10):
        word = do_step(word, rules)
        #print(i+1, word)

    cnt = Counter(word)
    most = cnt.most_common()[0][1]
    least = cnt.most_common()[-1][1]
    print(most - least)


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