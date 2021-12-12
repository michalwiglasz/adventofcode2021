#!/usr/bin/env python3

from pprint import pprint
from collections import defaultdict, Counter


def load():
    nodes = set()
    netlist = defaultdict(set)
    with open('12.txt', 'rt') as f:
        for line in f:
            a, b = line.strip().split('-')
            netlist[b].add(a)
            netlist[a].add(b)
            nodes.update({a, b})
    return nodes, netlist


def main():
    nodes, netlist = load()
    paths = find_paths(['start'], netlist)
    #pprint(sorted(paths))
    print(len(paths))


def find_paths(path, netlist):
    node = path[-1]

    if node == 'end':
        return [path]

    paths = []
    for target in netlist[node]:
        if can_visit(path, target):
            paths.extend(find_paths(path + [target], netlist))
    return paths


def can_visit(path, node):
    if node == 'start':
        return False
    elif node == 'end':
        return True
    elif is_small(node):
        small_count = Counter(n for n in path if is_small(n))
        if small_count[node] == 0:
            return True
        elif small_count[node] == 1:
            return not any(c > 1 for c in small_count.values())
        else:
            return False
    else:
        return True


def is_small(node):
    return node == node.lower()


if __name__ == '__main__':
    main()