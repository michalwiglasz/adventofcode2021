#!/usr/bin/env python3


CHUNK_TYPES = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

CHAR_SCORE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def main():
    score = 0
    with open('10.txt', 'rt') as f:
        for line in f:
            score += check_line(line.strip())
    print(score)


def check_line(line):
    stack = []

    for char in line:
        if char in CHUNK_TYPES:
            stack.append(CHUNK_TYPES[char])
        elif stack and char == stack.pop():
            continue
        else:
            return CHAR_SCORE[char]

    return 0



if __name__ == '__main__':
    main()