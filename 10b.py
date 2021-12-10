#!/usr/bin/env python3


CHUNK_TYPES = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

CHAR_SCORE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def main():
    scores = []
    with open('10.txt', 'rt') as f:
        for line in f:
            line_score = check_line(line.strip())
            if line_score is not None:
                scores.append(line_score)

    scores = list(sorted(scores))
    median = scores[len(scores) // 2]
    print(median)


def check_line(line):
    stack = []

    for char in line:
        if char in CHUNK_TYPES:
            stack.append(CHUNK_TYPES[char])
        elif stack and char == stack.pop():
            continue
        else:
            return None

    score = 0
    for char in reversed(stack):
        score = score * 5 + CHAR_SCORE[char]
    return score



if __name__ == '__main__':
    main()