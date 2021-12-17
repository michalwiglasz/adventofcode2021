#!/usr/bin/env python3

OP_LITERAL = 4

version_sum = 0


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
    read = parse_packet(data)
    print(f"read {read} bits, version sum {version_sum}")


def read_bits(data, pos, length, to_int=True):
    read = data[pos : pos+length]
    pos += length
    if to_int:
        return pos, int(read, 2)
    else:
        return pos, read


def parse_packet(data):
    pos = 0
    pos, version = read_bits(data, pos, 3)
    pos, op = read_bits(data, pos, 3)
    print(f"version {version}, op {op}", end="")

    global version_sum
    version_sum += version

    if op == OP_LITERAL:
        num = 0
        not_last = True
        while not_last:
            pos, not_last = read_bits(data, pos, 1)
            pos, digit = read_bits(data, pos, 4)
            num = (num << 4) + digit

        print(f", literal {num}")

    else:
        pos, length_type = read_bits(data, pos, 1)
        if length_type == 0:
            pos, bits = read_bits(data, pos, 15)
            print(f", subpackets {bits} bits")
            end = pos + bits
            while pos < end:
                pos += parse_packet(data[pos:])
        else:
            pos, subpackets = read_bits(data, pos, 11)
            print(f", subpackets {subpackets} times")
            for _ in range(subpackets):
                pos += parse_packet(data[pos:])

    return pos


if __name__ == '__main__':
    main()