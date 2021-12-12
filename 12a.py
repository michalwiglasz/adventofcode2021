#!/usr/bin/env python3

from pprint import pprint
from collections import defaultdict


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
    print(nodes)
    print(netlist)

    paths = find_paths(['start'], netlist)
    pprint(sorted(paths))
    print(len(paths))


def find_paths(path, netlist, level=0):
    node = path[-1]

    if node == 'end':
        return [path]

    paths = []
    for target in netlist[node]:
        if can_visit(path, target):
            paths.extend(find_paths(path + [target], netlist, level+1))
    return paths


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