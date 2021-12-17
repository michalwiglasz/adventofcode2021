#!/usr/bin/env python3

import math
from enum import Enum


class Op(Enum):
    SUM = 0
    MUL = 1
    MIN = 2
    MAX = 3
    LITERAL = 4
    GT = 5
    LT = 6
    EQ = 7


def load():
    data = []
    with open('16.txt', 'rt') as f:
        for line in f:
            for char in line.strip():
                binary = f'{int(char, 16):0>4b}'
                data.append(binary)
                #print(char, binary)
    return ''.join(data)


def main():
    data = load()
    print(data)
    bits, value = parse_packet(data)
    print(f"read {bits} bits, value {value}")


def read_bits(data, pos, length, to_int=True):
    read = data[pos : pos+length]
    pos += length
    if to_int:
        return pos, int(read, 2)
    else:
        return pos, read


def parse_packet(data):
    pos = 0
    value = 0

    pos, version = read_bits(data, pos, 3)
    pos, op = read_bits(data, pos, 3)
    op = Op(op)
    print(f"version {version}, op {op}", end="")

    if op == Op.LITERAL:
        not_last = True
        while not_last:
            pos, not_last = read_bits(data, pos, 1)
            pos, digit = read_bits(data, pos, 4)
            value = (value << 4) + digit

        print(f", literal {value}")

    else:
        pos, length_type = read_bits(data, pos, 1)
        values = []
        if length_type == 0:
            pos, bits = read_bits(data, pos, 15)
            print(f", subpackets {bits} bits")
            end = pos + bits
            while pos < end:
                p, v = parse_packet(data[pos:])
                pos += p
                values.append(v)
        else:
            pos, subpackets = read_bits(data, pos, 11)
            print(f", subpackets {subpackets} times")
            for _ in range(subpackets):
                p, v = parse_packet(data[pos:])
                pos += p
                values.append(v)

        if op == Op.SUM:
            value = sum(values)
        elif op == Op.MUL:
            value = math.prod(values)
        elif op == Op.MIN:
            value = min(values)
        elif op == Op.MAX:
            value = max(values)
        elif op == Op.GT:
            value = 1 if values[0] > values[1] else 0
        elif op == Op.LT:
            value = 1 if values[0] < values[1] else 0
        elif op == Op.EQ:
            value = 1 if values[0] == values[1] else 0

    return pos, value


if __name__ == '__main__':
    main()