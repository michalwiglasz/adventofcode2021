#!/usr/bin/env python3

import re
from  pprint import pprint


def load():
    boards = []

    with open('04.txt', 'rt') as f:
        numbers = [int(n) for n in f.readline().split(',')]

        board = []
        for line in (x.strip() for x in f):
            if not line:
                if board:
                    boards.append(board)
                board = []
                continue
            board.append([int(n) for n in re.split(r'\s+', line)])

        if board:
            boards.append(board)

    return boards, numbers


def check_boards(boards, called):
    for board in boards:
        if check_board(board, called):
            return board
    else:
        return None


def check_board(board, called):
    # check rows
    for row in board:
        if all(n in called for n in row):
            return True

    # check cols
    for cn in range(len(board)):
        col = [row[cn] for row in board]
        if all(n in called for n in col):
            return True

    return False

boards, numbers = load()
called = set()

for num in numbers:
    called.add(num)
    winner = check_boards(boards, called)

    if winner:
        unmarked_nums = [n for row in winner for n in row if n not in called]
        pprint(winner)
        print(unmarked_nums)
        score = sum(unmarked_nums) * num
        print(score)
        exit()